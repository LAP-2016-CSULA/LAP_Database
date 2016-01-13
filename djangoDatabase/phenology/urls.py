
from django.conf.urls import url
from phenology import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]