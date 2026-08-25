from .models import ContactEmail


def contact_email(request):
    return {"contact_email": ContactEmail.objects.first()}
