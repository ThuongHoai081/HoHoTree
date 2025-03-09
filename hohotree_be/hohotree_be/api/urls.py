from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("plant-disease/", include("hohotree_be.plant_disease.urls")),
    # path("auth/", include("hohotree_be.auth.urls")),
    # path("user/", include("hohotree_be.user.urls")),
]