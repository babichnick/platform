import os, time, datetime, uuid
from django.db import models 
from taggit.managers import TaggableManager
from django.utils.deconstruct import deconstructible

DEFAULT = 'nologo.jpg'


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        # eg: filename = 'my uploaded file.jpg'
        ext = filename.split('.')[-1]  #eg: '.jpg'
        uid = uuid.uuid4().hex[:10]    #eg: '567ae32f97'

        # eg: 'my-uploaded-file'
        new_name = '-'.join(filename.replace('.%s' % ext, '').split())

        # eg: 'my-uploaded-file_64c942aa64.jpg'
        renamed_filename = '%(new_name)s_%(uid)s.%(ext)s' % {'new_name': new_name, 'uid': uid, 'ext': ext}

        # eg: 'images/2017/01/29/my-uploaded-file_64c942aa64.jpg'
        return os.path.join(self.path, renamed_filename)

class Tool(models.Model):
   #abbreviation = models.CharField(max_length=50, help_text="Abbreviation of the app", default="", unique=True)
   name = models.CharField(max_length=100, help_text="name of app")
   slug = models.SlugField(unique=True) 

   description = models.TextField(default = "")
   logo = models.ImageField(default=DEFAULT, upload_to='protologo/')
   thumb = models.ImageField(upload_to=PathAndRename('toolimage/'), blank=True, null=True)
   website = models.CharField(max_length=300, help_text="website address", default="http://")

   TOOL_TYPE_CHOICES = (
         (1, 'Prototyping'),
         (2, 'Specification'), 
    )

   tool_type = models.IntegerField(choices=TOOL_TYPE_CHOICES, default=1)

   #published
   published = models.BooleanField(default = False, help_text="Tool is visible in the list")

   #price
   free = models.BooleanField(default = False, help_text="has a free version")
   cost_subscription = models.PositiveSmallIntegerField(null=True, blank=True, help_text="cheapest monthly payment")
   cost_purchase = models.PositiveSmallIntegerField(null=True, blank=True, help_text="one time cost")

   cost_text = models.CharField(max_length=300, help_text="Cost text information", default="")
   ideal_for = models.CharField(max_length=300, help_text="What this tools is great for", default="")
   
   works_offline = models.BooleanField(default = False, help_text="Tool doesn't require internet connection")

   last_updated = models.DateField(default='1987-06-03')

   #pros & cons
   pros = models.TextField(default = "")
   cons = models.TextField(default = "")

   #platform
   availablefor_web = models.BooleanField(default = False, help_text="Tool has a web version")
   availablefor_mac = models.BooleanField(default = False, help_text="Tool has a Mac version")
   availablefor_windows = models.BooleanField(default = False, help_text="Tool has Windows version")
   availablefor_linux = models.BooleanField(default = False, help_text="Tool has a Linux version")
   availablefor_ios = models.BooleanField(default = False, help_text="Tool has iOS version")
   availablefor_android = models.BooleanField(default = False, help_text="Tool has Android version")
 
   def __str__(self):
        return "%s" % self.name


class ToolImage(models.Model):

    tool = models.ForeignKey(Tool, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=PathAndRename('toolimage/'))

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
   voice = models.BooleanField(default = False, help_text="Prototyping for voice")

   #testing
   analytics = models.BooleanField(default = False, help_text="Can track events when testing")
   heatmaps = models.BooleanField(default = False, help_text="Generate heatmaps from user testing")
   sensors = models.BooleanField(default = False, help_text="Utilize device sensors")

   handoff = models.BooleanField(default = False, help_text="Generate specs automatically for developers")
   export_assets = models.BooleanField(default = False, help_text="CSS/XML styles can be exported")

   collaboration = models.BooleanField(default = False, help_text="Simultaneous editing")
   comments = models.BooleanField(default = False, help_text= "Team members can leave comments")

   import_from_photoshop = models.BooleanField(default = False, help_text="Import from Adobe Photoshop")
   import_from_sketch = models.BooleanField(default = False, help_text="Import from Sketch")
   import_from_dropbox = models.BooleanField(default = False, help_text="Import from Dropbox")
   import_from_mobile_camera = models.BooleanField(default = False, help_text="Import from Mobile Camera")

   def __str__(self):
        return "%s" % self.name


class Resource(models.Model):
   name = models.CharField(max_length=100, help_text="name of resource")
   slug = models.SlugField(unique=True) 
   description = models.TextField(default = "")
   header_image = models.ImageField(upload_to=PathAndRename('resourceimage/'), blank=True, null=True)
   link = models.CharField(max_length=300, help_text="link to resource", default="http://")
   tags = models.TextField(default = "")

   published = models.BooleanField(default = False, help_text="Resource is visible in the list")

   RESOURCE_TYPE_CHOICES = (
         (1, 'Fonts'),
         (2, 'Illustrations'), 
         (3, 'Icons'), 
         (4, 'Mockups'),
         (5, 'Web Templates'),
         (6, 'UI Kits'),
         (7, 'Photos'),    
    )

   resource_type = models.IntegerField(choices=RESOURCE_TYPE_CHOICES)

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
    slug = models.SlugField(max_length=200, default="",unique=True)
    tease = models.TextField()
    content = models.TextField(max_length=8000, default="")
    header_image = models.ImageField(upload_to=PathAndRename('publicationimage/'), blank=True, null=True)
    
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


class PublicationImage(models.Model):

    publication = models.ForeignKey(Publication, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=PathAndRename('publicationimage/'))


class Site(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    icon = models.ImageField(upload_to=PathAndRename('linkimage/'), blank=True, null=True)

    class Meta:
        verbose_name_plural = "Sites"
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return "%s" % self.name

class Link(models.Model):
  title = models.CharField(max_length=500, default="")
  slug = models.SlugField(max_length=200, default="",unique=True)
  header_image = models.ImageField(upload_to=PathAndRename('linkimage/'), blank=True, null=True)
  tease = models.TextField()
  tags = models.CharField(max_length=500, default="")
  site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True)
  url = models.CharField(max_length=300, help_text="link to resource", default="http://")
  pub_date = models.DateTimeField(default=datetime.datetime.now)
  published = models.BooleanField(default = False, help_text="Link is visible in the list")

  def __str__(self):
    return "%s" % self.name
 


class City(models.Model):

    REGION_CHOICES = (
         (1, 'Europe'),
         (2, 'North America'), 
         (3, 'South America'), 
         (4, 'Middle East'), 
         (5, 'Africa'), 
         (6, 'Asia'), 
         (7, 'Oceania'), 
    )


    class Meta:
        verbose_name_plural = "Cities"

    title = models.CharField(max_length=200, default="")
    slug = models.SlugField(max_length=200, default="")

    country = models.CharField(max_length=200, default="")
    region = models.IntegerField(choices=REGION_CHOICES, default=1)

    lat = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    lng = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)

    def __str__(self):
        return self.title


class Conference(models.Model):

    STATUS_CHOICES = (
         (1, 'Draft'),
         (2, 'Public'), 
    )

    class Meta:
        verbose_name_plural = "Conferences"

    title = models.CharField(max_length=500, default="")
    slug = models.SlugField(max_length=200, default="")

    pub_date = models.DateTimeField(default=datetime.datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    tease = models.TextField()
    content = models.TextField(max_length=8000, default="")

    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    from_date = models.DateField(default=datetime.datetime.now)
    to_date = models.DateField(default=datetime.datetime.now)

    logo = models.ImageField(default=DEFAULT, upload_to='conflogo/')
    website = models.CharField(max_length=300, help_text="website address", default="http://")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/conferences/%s/" % self.slug

class Contact(models.Model):
  full_name = models.CharField(max_length=120, null=True, blank=True)
  email = models.EmailField(null=True, blank=True)
  message = models.TextField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return self.full_name

