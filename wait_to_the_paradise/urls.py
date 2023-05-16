from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('wtp_open.urls')),
    path('wtp/', include('wtp.urls')),
    path('board/', include('board.urls')),
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('accounts/', include('allauth.urls')),

]
