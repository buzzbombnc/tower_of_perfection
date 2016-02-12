from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.core.urlresolvers import reverse

# Markdown and the defaults.
import markdown

markdown_defaults = {
    'extensions': ['markdown.extensions.extra', 'markdown.extensions.sane_lists'],
    'output_format': 'html5',
    'lazy_ol': False,
}

# TODO: Move this to settings?

class PublishedBlog(models.Manager):
    def get_queryset(self):
        return super(PublishedBlog, self).get_queryset().filter(published=True)


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    # Will be handled in the save method.
    slug = models.SlugField(blank=True, max_length=255)
    # This uses a callable default to allow us to change it.
    publish_date = models.DateTimeField(default=timezone.now)
    # Will be handled in the save method.
    update_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField()
    article = models.TextField()

    objects = models.Manager()
    published_objects = PublishedBlog()

    def __unicode__(self):
        i = "Blog '%s' from %s (" % (self.title, self.publish_date)
        if self.published: i += 'published, '
        i += '%d bytes)' % len(self.article)
        return i

    def save(self, *args, **kwargs):
        # slug is based on the title.
        if not self.slug:
            self.slug = slugify(self.title)

        # update_date is set based on whether the article is published or not.
        if self.published:
            self.update_date = timezone.now()
        else:
            self.update_date = None

        # Call the parent method.
        super(Blog, self).save(*args, **kwargs)

    def formatted_article(self):
        return markdown.markdown(self.article, **markdown_defaults)

    def get_absolute_url(self):
        return reverse('blog_entry', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-publish_date']

