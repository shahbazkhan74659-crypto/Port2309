from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Post, Project, Tag


def project_list(request):
    projects = Project.objects.all()

    category = request.GET.get("category", "").strip()
    if category:
        projects = projects.filter(category=category)

    tag = request.GET.get("tag", "").strip()
    if tag:
        projects = projects.filter(tags__name=tag)

    query = request.GET.get("q", "").strip()
    if query:
        projects = projects.filter(
            Q(title__icontains=query)
            | Q(short_description__icontains=query)
            | Q(description__icontains=query)
        )

    projects = projects.distinct()

    categories = (
        Project.objects.exclude(category="")
        .values_list("category", flat=True)
        .distinct()
        .order_by("category")
    )
    tags = Tag.objects.filter(projects__isnull=False).distinct().order_by("name")

    paginator = Paginator(projects, 9)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(
        request,
        "pages/projects.html",
        {
            "page_obj": page_obj,
            "projects": page_obj.object_list,
            "categories": categories,
            "tags": tags,
            "selected_category": category,
            "selected_tag": tag,
            "query": query,
        },
    )


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "pages/project_detail.html", {"project": project})


def blog_list(request):
    return render(request, "pages/blog.html", {"posts": Post.objects.all()})


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "pages/blog_detail.html", {"post": post})
