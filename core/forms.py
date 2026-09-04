from django import forms

from .models import ContactRequest, Feedback, HireRequest


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ["name", "email", "message"]


class HireRequestForm(forms.ModelForm):
    class Meta:
        model = HireRequest
        fields = ["name", "email", "project_type", "details", "budget", "timeline"]


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "rating", "feedback"]
        widgets = {"rating": forms.RadioSelect}
