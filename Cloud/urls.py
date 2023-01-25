from django.contrib import admin
from django.urls import path, include
from test_cloud.views import base_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('test_cloud/', include('test_cloud.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),
]
