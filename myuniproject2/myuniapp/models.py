from django.db import models

# Create your models here.
# class Profile(models.Model):
#     image = models.ImageField(default='profile.jpg', upload_to='profile_pictures')
#     contact_number = models.charfield(max_length = 12, default = "+989123456789")

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)

