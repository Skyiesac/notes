from django.contrib import admin
from . import models

class Notesinadmin(admin.ModelAdmin):
  list_display = ('title',)

admin.site.register(models.Notes, Notesinadmin)
