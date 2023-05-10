from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('wtp/', include('wtp.urls')),
    path('admin/', admin.site.urls),
]
