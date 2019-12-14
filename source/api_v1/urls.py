from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
]