from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserAPIView


router = DefaultRouter() if settings.DEBUG else SimpleRouter()


router.register("users", UserAPIView, basename='users-view')


app_name = "users.api"


urlpatterns = [
    path("", include(router.urls)),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
