from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),

]
