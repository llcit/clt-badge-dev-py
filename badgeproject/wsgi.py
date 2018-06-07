import os, sys

sys.path.append('/files/python3apps/cltbadges_env/')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "badgeproject.settings.base")

application = get_wsgi_application()
