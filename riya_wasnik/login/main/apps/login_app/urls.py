
from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.home ),
    url(r'^create$', views.process),
    url(r'^success$', views.success),
    url(r'^login$', views.login)
]
