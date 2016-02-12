from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Blog

class BlogIndex(ListView):
    template_name = 'blog_index.html'
    context_object_name = 'blogs'
    queryset = Blog.published_objects.all()


class BlogEntry(DetailView):
    template_name = 'blog_entry.html'
    context_object_name = 'entry'

    # Only authenticated users (admins) can view unpublished entries.
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Blog.objects.all()
        else:
            return Blog.published_objects.all()
