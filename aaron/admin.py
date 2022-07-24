from django.contrib import admin
from .models import AaronsTag

@admin.register(AaronsTag)
class AaronsTagAdmin(admin.ModelAdmin):
    pass