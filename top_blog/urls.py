from django.conf.urls import url
from .views import BlogIndex, BlogEntry

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)$', BlogEntry.as_view()),
    url(r'^(?P<slug>[\w-]+)$', BlogEntry.as_view(), name='blog_entry'),
    url(r'^$', BlogIndex.as_view(), name='blog_index'),
]
