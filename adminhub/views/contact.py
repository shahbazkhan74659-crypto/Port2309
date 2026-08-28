from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from core.models import ContactEmail, ContactRequest

from ..decorators import hub_staff_required
from ..forms import ContactEmailForm
from ._shared import singleton_delete_view, singleton_edit_view


@hub_staff_required
def contact_hub(request):
    contact_email = ContactEmail.objects.first()
    submissions = ContactRequest.objects.all()
    return render(
        request, "adminhub/contact.html", {"contact_email": contact_email, "submissions": submissions}
    )


@hub_staff_required
def contact_email_edit(request):
    next_url = request.GET.get("next") or request.POST.get("next") or "adminhub:contact"
    return singleton_edit_view(
        request, ContactEmail, ContactEmailForm, "adminhub/contact_email_form.html", next_url
    )


@hub_staff_required
def contact_email_delete(request):
    next_url = request.GET.get("next") or request.POST.get("next") or "adminhub:contact"
    return singleton_delete_view(
        request, ContactEmail, next_url,
        "Delete contact details?",
        "This affects the Home CTA, Contact, and Hire Me pages simultaneously.",
    )


@hub_staff_required
@require_POST
def contact_request_delete(request, pk):
    submission = get_object_or_404(ContactRequest, pk=pk)
    submission.delete()
    return redirect("adminhub:contact")
