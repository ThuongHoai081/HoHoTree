from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("plant-disease/", include("hohotree_be.plant_disease.urls")),
    path("auth/", include("hohotree_be.users.urls")),
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),
    path("auth/refresh-token/", TokenRefreshView.as_view(), name="refresh_token"),
]