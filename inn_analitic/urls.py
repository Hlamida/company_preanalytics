from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('ask.urls', namespace='ask')),
    path('admin/', admin.site.urls),
]
