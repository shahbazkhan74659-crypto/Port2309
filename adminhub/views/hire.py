from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from core.models import ContactEmail, HireRequest

from ..decorators import hub_staff_required


@hub_staff_required
def hire_hub(request):
    contact_email = ContactEmail.objects.first()
    submissions = HireRequest.objects.all()
    return render(
        request, "adminhub/hire.html", {"contact_email": contact_email, "submissions": submissions}
    )


@hub_staff_required
@require_POST
def hire_request_delete(request, pk):
    submission = get_object_or_404(HireRequest, pk=pk)
    submission.delete()
    return redirect("adminhub:hire")
