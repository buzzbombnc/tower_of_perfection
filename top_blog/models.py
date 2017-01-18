from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.core.urlresolvers import reverse

import top_markdown

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
        i = "'%s' - %d bytes - %s" % (self.title, len(self.article), self.publish_date)
        if self.published: i += '- published'
        return i

    def save(self, *args, **kwargs):
        # slug is based on the title.
        if not self.slug:
            self.slug = slugify(self.title)

        # Call the parent method.
        super(Blog, self).save(*args, **kwargs)

    def formatted_article(self):
        return top_markdown.format(self)

    def formatted_preview(self):
        # Watch the Windows line endings and split on Markdown paragraphs.
        article = self.article.replace('\r', '').split('\n\n')
        # Limit to 2 paras.
        if len(article) >= 2:
            article = article[:2]
        article = '\n\n'.join(article)
        return top_markdown.format(self, article)

    def get_absolute_url(self):
        return reverse('blog_entry', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-publish_date']


def blogimages_directory(instance, filename):
    # Store the images for a given article in a private directory.
    return "blog/%s/%s" % (instance.blog.id, filename)

class BlogImages(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=blogimages_directory)

    # TODO: Delete file on instance delete.
