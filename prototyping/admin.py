from prototyping.models import Tool, PrototypingTool 
from django.contrib import admin

class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'published')
    list_filter = ['published']

class PrototypingToolAdmin(admin.ModelAdmin):
    list_display = ('name','published')
    list_filter = ['published']
    #exclude = ('abbreviation', 'name', 'description', 'logo', 'website', 'published', 'free', 'cost_subscription', 'cost_purchase', 'works_offline', 'last_updated', 'availablefor_web', 'availablefor_mac', 'availablefor_windows', 'availablefor_linux', 'availablefor_ios', 'availablefor_android',)



# Register your models here.
admin.site.register(Tool, ToolAdmin)
admin.site.register(PrototypingTool, PrototypingToolAdmin)

#class PrototypingToolInline(admin.TabularInline):
#    model = PrototypingTool
#
#class ToolAdmin(admin.ModelAdmin):
#    inlines = [PrototypingToolInline] # (, a list of classes here such as PrototypingToolInline in round brackets
#
#admin.site.register(Tool, ToolAdmin)

