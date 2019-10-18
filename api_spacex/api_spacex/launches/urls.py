from django.urls import path, include
from api_spacex.launches.views import LatestLaunch, NextLaunch, UpcomingLaunches, PastLaunches, OneLaunch


urlpatterns = [
    path('latest', LatestLaunch().as_view(), name='launch-latest'),
    path('next', NextLaunch().as_view(), name='launch-next'),
    path('upcoming', UpcomingLaunches().as_view(), name='launch-upcoming'),
    path('past', PastLaunches().as_view(), name='launch-past'),
    path('<int:pk>', OneLaunch().as_view(), name='launch-one')
]
