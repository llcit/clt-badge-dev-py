def site_root(request):
    from django.conf import settings
    return {'SITE_ROOT': settings.SITE_ROOT}