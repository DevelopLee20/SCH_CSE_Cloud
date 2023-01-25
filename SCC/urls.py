from django.urls import path
from . import views
from .views import base_views, content_views

app_name = 'SCC'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('download/', content_views.file_download, name='file_download'),

    # content_views.py
    path('content/create/', content_views.content_create, name='content_create'),
    path('content/create/upload_file', content_views.content_create, name='content_create'),
    path('content/delete/<int:content_id>/', content_views.content_delete, name='content_delete'),
]