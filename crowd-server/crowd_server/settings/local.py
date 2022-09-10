# flake8: noqa

from .base import *

INSTALLED_APPS += ["debug_toolbar",
                   "crowd_server.apps.food_labeler" ,
                   "crowd_server.apps.image_caption",
                   "crowd_server.apps.food_fact",
                   "crowd_server.apps.sentiment",
                   ]
                   
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
