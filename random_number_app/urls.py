from django.urls import path
from . import views

urlpatterns = [
    path('', views.RandomNumber.as_view())
]