from django.urls import path, include
from rest_framework import routers
from launches.views import LatestLaunch, NextLaunch, UpcomingLaunches, PastLaunches, OneLaunch


urlpatterns = [
    path('latest', LatestLaunch().as_view()),
    path('next', NextLaunch().as_view()),
    path('upcoming', UpcomingLaunches().as_view()),
    path('past', PastLaunches().as_view()),
    path('<int:pk>', OneLaunch().as_view())
]
