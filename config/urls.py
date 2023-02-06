from django.urls import path, include
from django.contrib import admin
from SCC.views import base_views, content_views
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path('SCC/', include('SCC.urls')),          # localhost:8000/SCC
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),   # localhost:8000/
    #path('', include('SCC.urls')),
    path('download/', content_views.file_download, name='file_download'),
]