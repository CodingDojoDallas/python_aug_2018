from django.conf.urls import url
from  apps.city_app import views

urlpatterns=[
	url(r'^$', views.index)
]
