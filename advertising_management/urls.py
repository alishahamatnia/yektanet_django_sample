from django.contrib import admin
from django.urls import path
from advertising_management.views import ShowAdView, RedirectToAdLinkView

urlpatterns = [
    path('ads/', ShowAdView.as_view()),
    path('ads/click/<int:pk>/', RedirectToAdLinkView.as_view()),

]
