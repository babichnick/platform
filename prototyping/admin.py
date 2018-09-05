from prototyping.models import PrototypingTool 
from django.contrib import admin


class PrototypingToolAdmin(admin.ModelAdmin):
    list_display = ('name','published')
    list_filter = ['published']

# Register your models here.
admin.site.register(PrototypingTool, PrototypingToolAdmin)

