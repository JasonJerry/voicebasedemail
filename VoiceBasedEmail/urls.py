from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^inbox/$', views.inbox, name="inbox"),
    url(r'^read/$', views.read, name="read"),
    url(r'^compose/$', views.compose, name="compose"),
]
