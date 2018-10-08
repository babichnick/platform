from prototyping.models import Tool, PrototypingTool, Author, Category, Publication, City, Conference
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'published')
    list_filter = ['published']

class PrototypingToolAdmin(admin.ModelAdmin):
    list_display = ('name','published')
    list_filter = ['published']
    #exclude = ('abbreviation', 'name', 'description', 'logo', 'website', 'published', 'free', 'cost_subscription', 'cost_purchase', 'works_offline', 'last_updated', 'availablefor_web', 'availablefor_mac', 'availablefor_windows', 'availablefor_linux', 'availablefor_ios', 'availablefor_android',)

class AuthorAdmin(admin.ModelAdmin):
    list_diplay = ('full_name',)

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CityAdmin(admin.ModelAdmin):
    list_diplay = ('title',)

class ConferenceAdmin(admin.ModelAdmin):
    list_diplay = ('title',)

# Register your models here.
admin.site.register(Tool, ToolAdmin)
admin.site.register(PrototypingTool, PrototypingToolAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publication, PublicationAdmin)

admin.site.register(City, CityAdmin)
admin.site.register(Conference, ConferenceAdmin)


#class PrototypingToolInline(admin.TabularInline):
#    model = PrototypingTool
#
#class ToolAdmin(admin.ModelAdmin):
#    inlines = [PrototypingToolInline] # (, a list of classes here such as PrototypingToolInline in round brackets
#
#admin.site.register(Tool, ToolAdmin)

