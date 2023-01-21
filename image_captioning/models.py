from django.db import models


# Create your models here.

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.image.name
