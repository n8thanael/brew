from django.contrib import admin
from .models import AaronsTag

class AaronsTagAdmin(admin.ModelAdmin):
    pass
admin.site.register(AaronsTag, AaronsTagAdmin)