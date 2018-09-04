from django.db import models 

class PrototypingTool(models.Model):
   name = models.CharField(max_length=100, help_text="name of app")
   free = models.BooleanField(help_text="has a free version")
   
   cost_subscription = models.PositiveSmallIntegerField(default=1987)
   cost_purchase = models.PositiveSmallIntegerField(default=1987)

   last_updated = models.DateField(default='1987-06-03')

   availablefor_web = models.BooleanField(help_text="tool has a web version")
   availablefor_ios = models.BooleanField(help_text="tool has iOS version")
   availablefor_android = models.BooleanField(help_text="tool has Android version")
   availablefor_windows = models.BooleanField(help_text="tool has Windows version")
   availablefor_linux = models.BooleanField(help_text="tool has a Linux version")
   
