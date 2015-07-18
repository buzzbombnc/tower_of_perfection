from django.db import models
from django.conf import settings
from django.utils import timezone


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    # This uses a callable default to allow us to change it.
    publish_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField()
    article = models.TextField()


