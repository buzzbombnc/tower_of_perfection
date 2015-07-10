from django.views.generic.base import TemplateView

class Blog(TemplateView):
    template_name = 'blog.html'

