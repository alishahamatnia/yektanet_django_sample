from django.contrib import admin
from django.urls import path
from advertising_management.views import ShowAdView, RedirectToAdLinkView, CreateAdView

urlpatterns = [
    path('ads/', ShowAdView.as_view()),
    path('ads/click/<int:pk>/', RedirectToAdLinkView.as_view()),
    path('ads/create', CreateAdView.as_view()),

]
