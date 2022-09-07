from django.contrib import admin
from .models import Shortener
from .models import VisitUrl


admin.site.register(Shortener)
admin.site.register(VisitUrl)
