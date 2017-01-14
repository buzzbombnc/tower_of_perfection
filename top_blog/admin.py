from django.contrib import admin
import models

def article_size(obj):
    return len(obj.article)
article_size.short_description = 'Article Size'

class BlogImagesInline(admin.StackedInline):
    model = models.BlogImages
    verbose_name_plural = verbose_name = "Blog Images"


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
    list_display = ('title', article_size, 'published', 'publish_date', 'update_date')
    list_filter = ('published', 'publish_date')
    save_as = True
    fields = ('author', ('title', 'slug'), ('publish_date', 'update_date'), 'published', 'article')
    inlines = [BlogImagesInline,]

