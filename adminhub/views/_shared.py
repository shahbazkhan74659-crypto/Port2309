from django.shortcuts import redirect, render, resolve_url
from django.utils.http import url_has_allowed_host_and_scheme

from ..utils import apply_tag_quick_add


def resolve_next(request, default_url_name):
    """Where Save/Cancel on an edit page should return to: the page the user
    clicked Edit from. An explicit `next` (a querystring on the initial GET,
    replayed as a hidden field on every POST) wins — needed where one edit
    link is shared by more than one page, e.g. ContactEmail, linked from both
    Contact and Hire Me — otherwise falls back to the HTTP Referer captured
    on that initial GET, then to `default_url_name`."""
    candidate = (
        request.POST.get("next") or request.GET.get("next") or request.META.get("HTTP_REFERER")
    )
    if candidate and url_has_allowed_host_and_scheme(
        candidate, allowed_hosts={request.get_host()}, require_https=request.is_secure()
    ):
        return candidate
    return resolve_url(default_url_name)


def singleton_edit_view(request, model, form_class, template_name, success_url_name):
    """Shared GET/POST handler for the site's single-row 'settings' models
    (HeroContent, Quote, AboutSnapshot, About, ContactEmail, Resume,
    ResumePage). Creates the row on first save if none exists yet."""
    instance = model.objects.first()
    next_url = resolve_next(request, success_url_name)
    if request.method == "POST":
        quick_add_data = apply_tag_quick_add(request.POST)
        if quick_add_data is not None:
            form = form_class(quick_add_data, request.FILES, instance=instance)
            return render(request, template_name, {"form": form, "next_url": next_url})
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(next_url)
    else:
        form = form_class(instance=instance)
    return render(request, template_name, {"form": form, "next_url": next_url})


def singleton_delete_view(request, model, success_url_name, title, warning_message):
    instance = model.objects.first()
    if request.method == "POST":
        if instance is not None:
            instance.delete()
        return redirect(success_url_name)
    return render(
        request,
        "adminhub/confirm_delete.html",
        {
            "title": title,
            "warning_message": warning_message,
            "cancel_url": resolve_url(success_url_name),
        },
    )


def object_delete_view(request, obj, success_url_name, title, warning_message):
    if request.method == "POST":
        obj.delete()
        return redirect(success_url_name)
    return render(
        request,
        "adminhub/confirm_delete.html",
        {
            "title": title,
            "warning_message": warning_message,
            "cancel_url": resolve_url(success_url_name),
        },
    )
