from django.views.generic.list import ListView
from .models import Blog

class BlogIndex(ListView):
    template_name = 'blog_index.html'
    context_object_name = 'blogs'
    queryset = Blog.published_objects.all()
