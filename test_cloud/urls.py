from django.urls import path
from . import views
from .views import base_views, content_views

app_name = 'test_cloud'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:content_id>/', base_views.detail, name='detail'),

    # content_views.py
    path('content/create/', content_views.content_create, name='content_create'),
    path('content/modify/<int:content_id>/', content_views.content_modify, name='content_modify'),
    path('content/delete/<int:content_id>/', content_views.content_delete, name='content_delete'),
]