from django.contrib import admin
from .models import Shortener
from .models import VisitUrl


# Register your models here.
admin.site.register(Shortener)
admin.site.register(VisitUrl)