from django.urls import path, include
from django.contrib import admin
from SCC.views import base_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('SCC/', include('SCC.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),
]
