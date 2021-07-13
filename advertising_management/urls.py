from django.contrib import admin
from django.urls import path
from advertising_management.views import ShowAdView
urlpatterns = [
    path('ads/', ShowAdView.as_view()),
]
