from django.conf.urls import url
from .views import Blog, BlogIndex

urlpatterns = [
    url(r'', BlogIndex.as_view(), name='blog_index'),
]
