from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Action)
admin.site.register(models.Log)
admin.site.register(models.Bank)
admin.site.register(models.Ticket)
admin.site.register(models.Value)
admin.site.register(models.Style)
