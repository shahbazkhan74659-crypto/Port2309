import requests
from django.core.cache import cache
from django.shortcuts import redirect, render

from projects.models import Project

from .forms import ContactRequestForm, HireRequestForm
from .models import About, AboutSnapshot, HeroContent, Quote, Resume

GITHUB_USERNAME = "shahbazkhan74659-crypto"
GITHUB_CACHE_TTL = 60 * 15


def home(request):
    featured = Project.objects.filter(featured=True).first()
    hero = HeroContent.objects.first()
    quote = Quote.objects.first()
    about_snapshot = AboutSnapshot.objects.first()
    return render(
        request,
        "pages/home.html",
        {"featured": featured, "hero": hero, "quote": quote, "about_snapshot": about_snapshot},
    )


def about(request):
    about = About.objects.first()
    return render(request, "pages/about.html", {"about": about})


def _handle_lead_form(request, form_class, template_name):
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{request.path}?sent=1")
        for name in form.errors:
            if name in form.fields:
                widget = form.fields[name].widget
                widget.attrs["aria-invalid"] = "true"
                widget.attrs["aria-describedby"] = f"{form[name].id_for_label}-error"
    else:
        form = form_class()
    return render(request, template_name, {"form": form, "sent": request.GET.get("sent") == "1"})


def contact(request):
    return _handle_lead_form(request, ContactRequestForm, "pages/contact.html")


def hire_me(request):
    return _handle_lead_form(request, HireRequestForm, "pages/hire.html")


def resume(request):
    latest = Resume.objects.first()
    resume_url = latest.file.url if latest else None
    return render(request, "pages/resume.html", {"resume_url": resume_url})


def github(request):
    context = {
        "avatar_url": None,
        "name": "Shahbaz Khan",
        "handle": GITHUB_USERNAME,
        "bio": "Developer, freelancer, and writer.",
        "public_repos": "—",
        "followers": "—",
        "following": "—",
        "html_url": f"https://github.com/{GITHUB_USERNAME}",
        "repos": [],
    }

    profile_cache_key = f"github_profile_{GITHUB_USERNAME}"
    data = cache.get(profile_cache_key)
    if data is None:
        try:
            response = requests.get(
                f"https://api.github.com/users/{GITHUB_USERNAME}",
                timeout=5,
                headers={"Accept": "application/vnd.github+json"},
            )
            response.raise_for_status()
            data = response.json()
            cache.set(profile_cache_key, data, GITHUB_CACHE_TTL)
        except requests.RequestException:
            data = None
    if data:
        context.update({
            "avatar_url": data.get("avatar_url"),
            "name": data.get("name") or context["name"],
            "handle": data.get("login", GITHUB_USERNAME),
            "bio": data.get("bio") or context["bio"],
            "public_repos": data.get("public_repos", context["public_repos"]),
            "followers": data.get("followers", context["followers"]),
            "following": data.get("following", context["following"]),
            "html_url": data.get("html_url", context["html_url"]),
        })

    repos_cache_key = f"github_repos_{GITHUB_USERNAME}"
    repos_data = cache.get(repos_cache_key)
    if repos_data is None:
        try:
            repos_response = requests.get(
                f"https://api.github.com/users/{GITHUB_USERNAME}/repos",
                params={"sort": "updated", "per_page": 100},
                timeout=5,
                headers={"Accept": "application/vnd.github+json"},
            )
            repos_response.raise_for_status()
            repos_data = repos_response.json()
            cache.set(repos_cache_key, repos_data, GITHUB_CACHE_TTL)
        except requests.RequestException:
            repos_data = None
    if repos_data:
        context["repos"] = [
            {
                "name": repo.get("name"),
                "description": repo.get("description"),
                "html_url": repo.get("html_url"),
                "language": repo.get("language"),
                "stars": repo.get("stargazers_count", 0),
            }
            for repo in repos_data
        ]

    return render(request, "pages/github.html", context)
