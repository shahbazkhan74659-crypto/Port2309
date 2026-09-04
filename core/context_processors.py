from .models import ContactEmail


def contact_email(request):
    return {"contact_email": ContactEmail.objects.first()}


def canonical_url(request):
    # request.path excludes the query string, so filtered/paginated URLs
    # (e.g. /projects/?category=...&page=2) canonicalize to the clean path.
    return {"canonical_url": request.build_absolute_uri(request.path)}
