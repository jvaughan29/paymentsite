from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('entryapp.urls')),
    path('entryapp/', include('entryapp.urls')),
    path('admin/', admin.site.urls),
]