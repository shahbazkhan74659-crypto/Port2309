from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST


def _safe_next(request, default_url_name="adminhub:home"):
    next_url = request.GET.get("next") or request.POST.get("next")
    if next_url and url_has_allowed_host_and_scheme(
        next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()
    ):
        return next_url
    return reverse(default_url_name)


def hub_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect("adminhub:home")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if not user.is_staff:
                form.add_error(None, "This account does not have Admin Hub access.")
            else:
                login(request, user)
                return redirect(_safe_next(request))
    else:
        form = AuthenticationForm(request)

    return render(request, "adminhub/login.html", {"form": form})


@require_POST
def hub_logout(request):
    logout(request)
    return redirect("adminhub:login")
