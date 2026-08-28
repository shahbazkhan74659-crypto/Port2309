from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from projects.models import Project

from ..decorators import hub_staff_required
from ..forms import ProjectForm, ProjectImageFormSet
from ..utils import apply_tag_quick_add
from ._shared import object_delete_view


@hub_staff_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, "adminhub/projects.html", {"projects": projects})


def _project_form_view(request, project=None):
    if request.method == "POST":
        quick_add_data = apply_tag_quick_add(request.POST)
        if quick_add_data is not None:
            form = ProjectForm(quick_add_data, request.FILES, instance=project)
            formset = ProjectImageFormSet(instance=project)
            return render(
                request, "adminhub/project_form.html", {"form": form, "formset": formset, "project": project}
            )

        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            with transaction.atomic():
                saved_project = form.save()
                formset = ProjectImageFormSet(request.POST, request.FILES, instance=saved_project)
                if formset.is_valid():
                    formset.save()
                else:
                    transaction.set_rollback(True)
            if formset.is_valid():
                return redirect("adminhub:project_list")
            return render(
                request, "adminhub/project_form.html", {"form": form, "formset": formset, "project": project}
            )

        # Main form invalid — re-show it; image edits aren't preserved on this path.
        formset = ProjectImageFormSet(instance=project)
        return render(
            request, "adminhub/project_form.html", {"form": form, "formset": formset, "project": project}
        )

    form = ProjectForm(instance=project)
    formset = ProjectImageFormSet(instance=project)
    return render(
        request, "adminhub/project_form.html", {"form": form, "formset": formset, "project": project}
    )


@hub_staff_required
def project_create(request):
    return _project_form_view(request, project=None)


@hub_staff_required
def project_edit(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return _project_form_view(request, project=project)


@hub_staff_required
def project_delete(request, slug):
    project = get_object_or_404(Project, slug=slug)
    image_count = project.images.count()
    warning = f"This will also delete {image_count} associated image(s)." if image_count else "This project has no images."
    return object_delete_view(
        request, project, "adminhub:project_list",
        f"Delete '{project.title}'?", warning,
    )
