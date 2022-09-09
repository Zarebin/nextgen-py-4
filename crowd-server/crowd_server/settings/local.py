# flake8: noqa

from .base import *

INSTALLED_APPS += ["debug_toolbar", "crowd_server.apps.food_fact"]

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"