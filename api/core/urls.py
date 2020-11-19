from django.urls import path, include
from .views import ArretViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'arrets', ArretViewSet)

urlpatterns = [
    path("", include(router.urls))
]