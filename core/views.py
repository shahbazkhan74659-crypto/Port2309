import requests
from django.shortcuts import redirect, render

from projects.models import Project

from .forms import ContactRequestForm, HireRequestForm
from .models import About, AboutSnapshot, HeroContent, Quote, Resume

GITHUB_USERNAME = "shahbazkhan74659-crypto"


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


def contact(request):
    if request.method == "POST":
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{request.path}?sent=1")
    else:
        form = ContactRequestForm()
    return render(request, "pages/contact.html", {"form": form, "sent": request.GET.get("sent") == "1"})


def hire_me(request):
    if request.method == "POST":
        form = HireRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"{request.path}?sent=1")
    else:
        form = HireRequestForm()
    return render(request, "pages/hire.html", {"form": form, "sent": request.GET.get("sent") == "1"})


def blog(request):
    return render(request, "pages/blog.html")


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
    try:
        response = requests.get(
            f"https://api.github.com/users/{GITHUB_USERNAME}",
            timeout=5,
            headers={"Accept": "application/vnd.github+json"},
        )
        response.raise_for_status()
        data = response.json()
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
    except requests.RequestException:
        pass

    try:
        repos_response = requests.get(
            f"https://api.github.com/users/{GITHUB_USERNAME}/repos",
            params={"sort": "updated", "per_page": 100},
            timeout=5,
            headers={"Accept": "application/vnd.github+json"},
        )
        repos_response.raise_for_status()
        context["repos"] = [
            {
                "name": repo.get("name"),
                "description": repo.get("description"),
                "html_url": repo.get("html_url"),
                "language": repo.get("language"),
                "stars": repo.get("stargazers_count", 0),
            }
            for repo in repos_response.json()
        ]
    except requests.RequestException:
        pass

    return render(request, "pages/github.html", context)
