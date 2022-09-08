from django.db import models
from django.forms import DateTimeField



# Create your models here.

class registrationmodel(models.Model):
    name = models.CharField( max_length=50)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    img = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name