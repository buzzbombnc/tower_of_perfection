from django.conf.urls import url
from .views import Blog

urlpatterns = [
    url(r'', Blog.as_view(), name='blog'),
]
