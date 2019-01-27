from django.urls import path,include
from joins import views
from django.conf.urls import url
urlpatterns = [
    path('', views.home,name='home'),
    url(r'^(?P<ref_id>.*)$', views.share, name='share'),
]
