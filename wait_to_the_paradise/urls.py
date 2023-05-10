from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('wtp_open.urls')),
    path('wtp/', include('wtp.urls')),
    path('admin/', admin.site.urls),
]
