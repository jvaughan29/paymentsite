from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('entry/', include('entry.urls')),
    path('admin/', admin.site.urls),
]