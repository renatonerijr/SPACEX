from django.urls import path, include

urlpatterns = [
    path('launches/', include('api_spacex.launches.urls'))
]
