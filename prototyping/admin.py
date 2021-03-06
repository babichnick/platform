from prototyping.models import Tool, ToolImage,PublicationImage, PrototypingTool, Author, Site, Link, Resource, Category, Publication, City, Conference, Contact, Video, BookCategory, Book, VideoCategory
from django.contrib import admin

from mptt.admin import MPTTModelAdmin
from prototyping.models import Toolbox, Toolboxcategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ToolImageInline(admin.TabularInline):
    model = ToolImage
    extra = 3

class PublicationImageInline(admin.TabularInline):
    model = PublicationImage
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


class ResourceAdmin(admin.ModelAdmin):
    list_diplay = ('name','published')
    list_filter = ['published']

class SiteAdmin(admin.ModelAdmin):
    list_diplay = ('name',)

class LinkAdmin(admin.ModelAdmin):
    list_diplay = ('title','published')
    list_filter = ['published']

class BookAdmin(admin.ModelAdmin):
    list_diplay = ('title','published')
    list_filter = ['published']

class AuthorAdmin(admin.ModelAdmin):
    list_diplay = ('full_name',)

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ['status']
    inlines = [ PublicationImageInline, ] 

class CityAdmin(admin.ModelAdmin):
    list_diplay = ('title',)

class ConferenceAdmin(admin.ModelAdmin):
    list_diplay = ('title',)

class VideoCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class VideoAdmin(admin.ModelAdmin):
    list_diplay = ('title',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','created')

#class CustomMPTTModelAdmin(MPTTModelAdmin):
#    mptt_indent_field = "name"


class ToolboxAdmin(admin.ModelAdmin):
    list_diplay = ('name',)

# Register your models here.
admin.site.register(Tool, ToolAdmin)
admin.site.register(PrototypingTool, PrototypingToolAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publication, PublicationAdmin)

admin.site.register(Resource, ResourceAdmin)

admin.site.register(City, CityAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoCategory, VideoCategoryAdmin)
admin.site.register(Contact, ContactAdmin)

admin.site.register(Site, SiteAdmin)
admin.site.register(Link, LinkAdmin)

admin.site.register(BookCategory, BookCategoryAdmin)
admin.site.register(Book, BookAdmin)

admin.site.register(Toolbox, ToolboxAdmin)
admin.site.register(Toolboxcategory, MPTTModelAdmin)

#class PrototypingToolInline(admin.TabularInline):
#    model = PrototypingTool
#
#class ToolAdmin(admin.ModelAdmin):
#    inlines = [PrototypingToolInline] # (, a list of classes here such as PrototypingToolInline in round brackets
#
#admin.site.register(Tool, ToolAdmin)

