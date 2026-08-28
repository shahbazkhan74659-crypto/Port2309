from django.shortcuts import render

from core.models import About

from ..decorators import hub_staff_required
from ..forms import AboutForm
from ._shared import singleton_delete_view, singleton_edit_view


@hub_staff_required
def about_hub(request):
    about = About.objects.first()
    return render(request, "adminhub/about.html", {"about": about})


@hub_staff_required
def about_edit(request):
    return singleton_edit_view(
        request, About, AboutForm, "adminhub/about_form.html", "adminhub:about"
    )


@hub_staff_required
def about_delete(request):
    return singleton_delete_view(
        request, About, "adminhub:about",
        "Delete the About page?",
        "The About page will be empty until you add new content.",
    )
