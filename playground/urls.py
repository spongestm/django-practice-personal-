from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns=[
    path('',views.empty_response),
    path('hello/',views.say_hello),
]