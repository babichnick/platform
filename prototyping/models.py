from django.db import models 
from taggit.managers import TaggableManager

import datetime

DEFAULT = 'nologo.jpg'


class Tool(models.Model):
   #abbreviation = models.CharField(max_length=50, help_text="Abbreviation of the app", default="", unique=True)
   name = models.CharField(max_length=100, help_text="name of app")
   slug = models.SlugField(unique=True) 

   description = models.TextField(default = "")
   logo = models.ImageField(default=DEFAULT, upload_to='protologo/')
   website = models.CharField(max_length=300, help_text="website address", default="http://")

   #published
   published = models.BooleanField(default = False, help_text="Tool is visible in the list")

   #price
   free = models.BooleanField(default = False, help_text="has a free version")
   cost_subscription = models.PositiveSmallIntegerField(default=1987, help_text="cheapest monthly payment")
   cost_purchase = models.PositiveSmallIntegerField(default=1987, help_text="one time cost")

   works_offline = models.BooleanField(default = False, help_text="Tool doesn't require internet connection")

   last_updated = models.DateField(default='1987-06-03')

   #platform
   availablefor_web = models.BooleanField(default = False, help_text="Tool has a web version")
   availablefor_mac = models.BooleanField(default = False, help_text="Tool has a Mac version")
   availablefor_windows = models.BooleanField(default = False, help_text="Tool has Windows version")
   availablefor_linux = models.BooleanField(default = False, help_text="Tool has a Linux version")
   availablefor_ios = models.BooleanField(default = False, help_text="Tool has iOS version")
   availablefor_android = models.BooleanField(default = False, help_text="Tool has Android version")
 
   def __str__(self):
        return "%s" % self.name

class PrototypingTool(Tool):
   #features
   design = models.BooleanField(default = False, help_text="App can design from scratch")
   artboards = models.BooleanField(default = False, help_text="Multiple visible artboards")
   symbols = models.BooleanField(default = False, help_text="Document-wide master symbols")
   responsive = models.BooleanField(default = False, help_text="Dynamically resizing groups")
   hotspots = models.BooleanField(default = False, help_text="")
   pen_tool = models.BooleanField(default = False, help_text="Draw paths")
   animations = models.BooleanField(default = False, help_text="Individual animations and microinteractions")
   transitions = models.BooleanField(default = False, help_text="Animation between screens")

   #testing
   analytics = models.BooleanField(default = False, help_text="Can track events when testing")
   heatmaps = models.BooleanField(default = False, help_text="Generate heatmaps from user testing")
   sensors = models.BooleanField(default = False, help_text="Utilize device sensors")

   handoff = models.BooleanField(default = False, help_text="Generate specs automatically for developers")
   export_assets = models.BooleanField(default = False, help_text="CSS/XML styles can be exported")

   collaboration = models.BooleanField(default = False, help_text="Simultaneous editing")
   comments = models.BooleanField(default = False, help_text= "Team members can leave comments")

   def __str__(self):
        return "%s" % self.name

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "%s" % (self.full_name)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return "%s" % self.name


class Publication(models.Model):

    STATUS_CHOICES = (
         (1, 'Draft'),
         (2, 'Public'), 
    )

    class Meta:
        verbose_name_plural = "Publications"
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'

    title = models.CharField(max_length=500, default="")
    slug = models.SlugField(max_length=200, default="")
    tease = models.TextField()
    content = models.TextField(max_length=8000, default="")
    
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, blank=True, null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/publications/%s/" % self.slug
