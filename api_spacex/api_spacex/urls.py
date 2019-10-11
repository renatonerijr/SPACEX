from django.urls import path, include

urlpatterns = [
    path('launches/', include('launches.urls'))
]
