######################################################################
##   Final Lab
##   Jacob Stoebel (stoebelj)
## CSC 326, Data Structures
## urls.py
## Purpose: Maps valid urls to their appropaite view in views.py
## Aknowledgements: (see readme.txt)


__author__ = 'stoebelj'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^show_node$', views.show_node, name='show_node'),
    url(r'^learn/(?P<node_id>[0-9]+)', views.learn, name='learn'),
    url(r'^learn_confirm', views.learn_confirm, name='learn_confirm')
]