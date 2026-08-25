from django import forms

from .models import ContactRequest, HireRequest


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ["name", "email", "message"]


class HireRequestForm(forms.ModelForm):
    class Meta:
        model = HireRequest
        fields = ["name", "email", "project_type", "details", "budget", "timeline"]
