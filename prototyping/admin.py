from prototyping.models import Tool, ToolImage, PrototypingTool, Author, Category, Publication, City, Conference, Contact
from django.contrib import admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)



class ToolImageInline(admin.TabularInline):
    model = ToolImage
    extra = 3

class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'published')
    list_filter = ['published']
    inlines = [ ToolImageInline, ] 

class PrototypingToolAdmin(admin.ModelAdmin):
    list_display = ('name','published')
    list_filter = ['published']
    inlines = [ ToolImageInline, ] 
    #exclude = ('abbreviation', 'name', 'description', 'logo', 'website', 'published', 'free', 'cost_subscription', 'cost_purchase', 'works_offline', 'last_updated', 'availablefor_web', 'availablefor_mac', 'availablefor_windows', 'availablefor_linux', 'availablefor_ios', 'availablefor_android',)

class AuthorAdmin(admin.ModelAdmin):
    list_diplay = ('full_name',)

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ['status']

class CityAdmin(admin.ModelAdmin):
    list_diplay = ('title',)

class ConferenceAdmin(admin.ModelAdmin):
    list_diplay = ('title',)

class ContactAdmin(admin.ModelAdmin):
    list_diplay = ('full_name','email','created')

# Register your models here.
admin.site.register(Tool, ToolAdmin)
admin.site.register(PrototypingTool, PrototypingToolAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publication, PublicationAdmin)

admin.site.register(City, CityAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Contact, ContactAdmin)


#class PrototypingToolInline(admin.TabularInline):
#    model = PrototypingTool
#
#class ToolAdmin(admin.ModelAdmin):
#    inlines = [PrototypingToolInline] # (, a list of classes here such as PrototypingToolInline in round brackets
#
#admin.site.register(Tool, ToolAdmin)

