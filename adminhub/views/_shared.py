from django.shortcuts import redirect, render, resolve_url

from ..utils import apply_tag_quick_add


def singleton_edit_view(request, model, form_class, template_name, success_url_name):
    """Shared GET/POST handler for the site's single-row 'settings' models
    (HeroContent, Quote, AboutSnapshot, About, ContactEmail, Resume,
    ResumePage). Creates the row on first save if none exists yet."""
    instance = model.objects.first()
    if request.method == "POST":
        quick_add_data = apply_tag_quick_add(request.POST)
        if quick_add_data is not None:
            form = form_class(quick_add_data, request.FILES, instance=instance)
            return render(request, template_name, {"form": form})
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url_name)
    else:
        form = form_class(instance=instance)
    return render(request, template_name, {"form": form})


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
