from django.shortcuts import get_object_or_404, redirect, render

from projects.models import Post

from ..decorators import hub_staff_required
from ..forms import PostForm
from ..utils import apply_tag_quick_add
from ._shared import object_delete_view, resolve_next


@hub_staff_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, "adminhub/blog.html", {"posts": posts})


def _post_form_view(request, post=None):
    next_url = resolve_next(request, "adminhub:post_list")
    if request.method == "POST":
        quick_add_data = apply_tag_quick_add(request.POST)
        if quick_add_data is not None:
            form = PostForm(quick_add_data, instance=post)
            return render(request, "adminhub/post_form.html", {"form": form, "post": post, "next_url": next_url})

        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(next_url)
        return render(request, "adminhub/post_form.html", {"form": form, "post": post, "next_url": next_url})

    form = PostForm(instance=post)
    return render(request, "adminhub/post_form.html", {"form": form, "post": post, "next_url": next_url})


@hub_staff_required
def post_create(request):
    return _post_form_view(request, post=None)


@hub_staff_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return _post_form_view(request, post=post)


@hub_staff_required
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return object_delete_view(
        request, post, "adminhub:post_list",
        f"Delete '{post.title}'?", "This cannot be undone.",
    )
