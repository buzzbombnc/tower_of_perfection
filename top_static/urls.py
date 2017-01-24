from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),
]
