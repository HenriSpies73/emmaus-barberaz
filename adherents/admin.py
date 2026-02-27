from django.contrib import admin
from .models import Adherent, Association

admin.site.register(Association)
admin.site.register(Adherent)