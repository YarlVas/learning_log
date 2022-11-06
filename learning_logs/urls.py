from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.get_topics, name='topics'),
    path(r'^topics/(?P<topic_id>\d+)/$', views.get_topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
