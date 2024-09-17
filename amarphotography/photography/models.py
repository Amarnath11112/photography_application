from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

# Create your models here.

class Photography(models.Model):
    img_photo = models.ImageField(upload_to='Photography/img', blank=False)
    img_title = models.CharField(max_length=128, blank=False)
    img_description = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return self.img_title

    class Meta:
        verbose_name_plural = "Photography"


class films(models.Model):
    film_video = models.FileField(upload_to='videos_uploaded', null=True,
                             validators=[
                                 FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    date_uploaded = models.DateTimeField(default=timezone.now)
    film_title = models.CharField(max_length=128, blank=False)
    film_description = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return self.img_title

    class Meta:
        verbose_name_plural = "films"



class Stories(models.Model):
    st_photo = models.ImageField(upload_to='images/', blank=True)
    st_title = models.CharField(max_length=128, blank=False)
    st_description = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return self.img_title

    class Meta:
        verbose_name_plural = "Stories"



