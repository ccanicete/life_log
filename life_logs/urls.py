"""Defines URL patterns for life_logs."""
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),

    # detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # edit an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
