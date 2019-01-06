from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.post_list_view),
    re_path(r'^posts/$', views.post_list_view, name='post'),
    re_path(r'^posts/(?P<id>\d+)/$', views.post_detail_view, name='post-detail'),
    re_path(r'^search/$', views.post_search_view, name='search'),

]