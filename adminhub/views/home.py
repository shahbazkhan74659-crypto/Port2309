from django.shortcuts import render

from core.models import AboutSnapshot, HeroContent, Quote
from projects.models import Project

from ..decorators import hub_staff_required
from ..forms import AboutSnapshotForm, HeroContentForm, QuoteForm
from ._shared import singleton_delete_view, singleton_edit_view


@hub_staff_required
def hub_home(request):
    hero = HeroContent.objects.first()
    quote = Quote.objects.first()
    about_snapshot = AboutSnapshot.objects.first()
    featured_projects = Project.objects.filter(featured=True)
    return render(
        request,
        "adminhub/home.html",
        {
            "hero": hero,
            "quote": quote,
            "about_snapshot": about_snapshot,
            "featured_projects": featured_projects,
        },
    )


@hub_staff_required
def hero_edit(request):
    return singleton_edit_view(
        request, HeroContent, HeroContentForm, "adminhub/hero_form.html", "adminhub:home"
    )


@hub_staff_required
def hero_delete(request):
    return singleton_delete_view(
        request, HeroContent, "adminhub:home",
        "Delete Hero Content?",
        "The Home page hero section will be empty until you add new content.",
    )


@hub_staff_required
def quote_edit(request):
    return singleton_edit_view(
        request, Quote, QuoteForm, "adminhub/quote_form.html", "adminhub:home"
    )


@hub_staff_required
def quote_delete(request):
    return singleton_delete_view(
        request, Quote, "adminhub:home",
        "Delete Quote?",
        "The Home page statement section will be empty until you add a new quote.",
    )


@hub_staff_required
def about_snapshot_edit(request):
    return singleton_edit_view(
        request, AboutSnapshot, AboutSnapshotForm, "adminhub/about_snapshot_form.html", "adminhub:home"
    )


@hub_staff_required
def about_snapshot_delete(request):
    return singleton_delete_view(
        request, AboutSnapshot, "adminhub:home",
        "Delete About Snapshot?",
        "The Home page 'A little about me' section will be empty until you add new content.",
    )
