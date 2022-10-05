from django.contrib import admin
from .models import EraseBackgroundModel


@admin.register(EraseBackgroundModel)
class EraseBackgroundAdmin (admin.ModelAdmin):
    list_display = ['id', 'image']
