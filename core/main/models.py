from django.db import models
import os


def content_file_name_artist(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_thumbnail.%s" % (instance.name, ext)
    return os.path.join('artist_thumbnail/', filename)

def content_file_name_artist_logo(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_logo.%s" % (instance.name, ext)
    return os.path.join('artist_logo/', filename)


class Artist(models.Model):
    name = models.CharField(max_length=128)
    desription = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to=content_file_name_artist, null=True, blank=True)
    logo = models.ImageField(upload_to=content_file_name_artist_logo, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    spotify = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    mail = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)

    def __str__(self):
        return self.name
