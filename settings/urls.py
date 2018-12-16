# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
import oauth2client.contrib.django_util.site as django_util_site

urlpatterns = [
    url(r'^', include('VoiceBasedEmail.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^oauth2/', django_util_site.urls)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
