from django.urls import include, path
from . import api, views

urlpatterns = [
    path('', views.index),
    path('file', api.list),
    path('file/<str:token>', api.download),
]
