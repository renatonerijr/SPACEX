from django.urls import path, include
from rest_framework import routers
from launches.views import LatestLaunche


urlpatterns = [
    path('latest', LatestLaunche().as_view())
]
