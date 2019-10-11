from django.urls import path, include
from rest_framework import routers
from launches.views import LatestLaunch, NextLaunch


urlpatterns = [
    path('latest', LatestLaunch().as_view()),
    path('next', NextLaunch().as_view())
]
