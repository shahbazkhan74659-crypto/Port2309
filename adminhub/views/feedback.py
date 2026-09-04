from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from core.models import Feedback, expire_viewed_feedback

from ..decorators import hub_staff_required


def _feedback_queue():
    return Feedback.objects.exclude(status="viewed")


def _is_ajax(request):
    return request.headers.get("X-Requested-With") == "XMLHttpRequest"


def _feedback_results_response(request):
    return render(request, "adminhub/partials/feedback_results.html", {"submissions": _feedback_queue()})


@hub_staff_required
def feedback_hub(request):
    return render(request, "adminhub/feedback.html", {"submissions": _feedback_queue()})


@hub_staff_required
def feedback_viewed_hub(request):
    expire_viewed_feedback()
    submissions = Feedback.objects.filter(status="viewed")
    return render(request, "adminhub/feedback_viewed.html", {"submissions": submissions})


@hub_staff_required
@require_POST
def feedback_publish(request, pk):
    entry = get_object_or_404(Feedback, pk=pk)
    entry.status = "live"
    entry.save(update_fields=["status"])
    if _is_ajax(request):
        return _feedback_results_response(request)
    return redirect("adminhub:feedback")


@hub_staff_required
@require_POST
def feedback_unpublish(request, pk):
    entry = get_object_or_404(Feedback, pk=pk)
    entry.status = "pending"
    entry.save(update_fields=["status"])
    if _is_ajax(request):
        return _feedback_results_response(request)
    return redirect("adminhub:feedback")


@hub_staff_required
@require_POST
def feedback_mark_viewed(request, pk):
    entry = get_object_or_404(Feedback, pk=pk)
    entry.status = "viewed"
    entry.viewed_at = timezone.now()
    entry.save(update_fields=["status", "viewed_at"])
    if _is_ajax(request):
        return _feedback_results_response(request)
    return redirect("adminhub:feedback")


@hub_staff_required
@require_POST
def feedback_delete(request, pk):
    entry = get_object_or_404(Feedback, pk=pk)
    entry.delete()
    if _is_ajax(request):
        return _feedback_results_response(request)
    return redirect(request.POST.get("next") or "adminhub:feedback")
