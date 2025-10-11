from django.db import models

class Upload(models.Model):
    filename = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, default=None)
    address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.filename