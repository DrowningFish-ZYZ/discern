from django.urls import path, include

urlpatterns = [
    path('api/1/', include('api1.urls'))
]
