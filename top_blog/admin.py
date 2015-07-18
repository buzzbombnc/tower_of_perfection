from django.contrib import admin
import models

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }

