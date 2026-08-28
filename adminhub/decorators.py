from django.contrib.auth.decorators import user_passes_test


def hub_staff_required(view_func):
    return user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url="adminhub:login",
    )(view_func)
