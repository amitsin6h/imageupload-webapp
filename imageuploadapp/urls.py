from django.conf.urls import url
from .import views

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^image_upload/$', views.image_uploaded, name='image_uploaded'),
]
