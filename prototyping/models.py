from django.db import models 

DEFAULT = 'nologo.jpg'


class Tool(models.Model):
   abbreviation = models.CharField(max_length=50, help_text="Abbreviation of the app", default="")
   name = models.CharField(max_length=100, help_text="name of app")
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

    def __str__(self):
        return "%s" % (self.full_name)

class Publication(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
