from django.shortcuts import get_object_or_404, redirect, render

from core.models import Resume, ResumeEducation, ResumeExperience, ResumePage

from ..decorators import hub_staff_required
from ..forms import ResumeEducationForm, ResumeExperienceForm, ResumeFileForm, ResumePageForm
from ..utils import apply_tag_quick_add
from ._shared import object_delete_view, singleton_delete_view, singleton_edit_view


@hub_staff_required
def resume_hub(request):
    latest_file = Resume.objects.first()
    resume_page = ResumePage.objects.first()
    experience = ResumeExperience.objects.all()
    education = ResumeEducation.objects.all()
    return render(
        request,
        "adminhub/resume.html",
        {
            "latest_file": latest_file,
            "resume_page": resume_page,
            "experience": experience,
            "education": education,
        },
    )


@hub_staff_required
def resume_file_edit(request):
    return singleton_edit_view(
        request, Resume, ResumeFileForm, "adminhub/resume_file_form.html", "adminhub:resume"
    )


@hub_staff_required
def resume_file_delete(request):
    return singleton_delete_view(
        request, Resume, "adminhub:resume",
        "Delete the Resume PDF?",
        "The public Download PDF button will fall back to the static placeholder path until you upload a new file.",
    )


@hub_staff_required
def resume_page_edit(request):
    return singleton_edit_view(
        request, ResumePage, ResumePageForm, "adminhub/resume_page_form.html", "adminhub:resume"
    )


@hub_staff_required
def resume_page_delete(request):
    return singleton_delete_view(
        request, ResumePage, "adminhub:resume",
        "Delete the Resume Skills section?",
        "The Resume page's intro line and Skills & Tools section will be empty until you add new content.",
    )


def _experience_form_view(request, entry=None):
    if request.method == "POST":
        form = ResumeExperienceForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect("adminhub:resume")
    else:
        form = ResumeExperienceForm(instance=entry)
    return render(request, "adminhub/resume_entry_form.html", {"form": form, "kind": "Experience"})


@hub_staff_required
def experience_create(request):
    return _experience_form_view(request, entry=None)


@hub_staff_required
def experience_edit(request, pk):
    entry = get_object_or_404(ResumeExperience, pk=pk)
    return _experience_form_view(request, entry=entry)


@hub_staff_required
def experience_delete(request, pk):
    entry = get_object_or_404(ResumeExperience, pk=pk)
    return object_delete_view(
        request, entry, "adminhub:resume",
        f"Delete '{entry.role} — {entry.organization}'?", "This cannot be undone.",
    )


def _education_form_view(request, entry=None):
    if request.method == "POST":
        form = ResumeEducationForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect("adminhub:resume")
    else:
        form = ResumeEducationForm(instance=entry)
    return render(request, "adminhub/resume_entry_form.html", {"form": form, "kind": "Education"})


@hub_staff_required
def education_create(request):
    return _education_form_view(request, entry=None)


@hub_staff_required
def education_edit(request, pk):
    entry = get_object_or_404(ResumeEducation, pk=pk)
    return _education_form_view(request, entry=entry)


@hub_staff_required
def education_delete(request, pk):
    entry = get_object_or_404(ResumeEducation, pk=pk)
    return object_delete_view(
        request, entry, "adminhub:resume",
        f"Delete '{entry.degree} — {entry.institution}'?", "This cannot be undone.",
    )
