from django.db import router
from django.urls import path,include
from rest_framework import routers
from .views import BluehavenViewSet

router=routers.DefaultRouter()
router.register("bluehaven",BluehavenViewSet)

urlpatterns=[
    path("",include(router.urls)),
]