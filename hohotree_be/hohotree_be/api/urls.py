from django.contrib import admin
from django.urls import path, include
from .views import RegisterView
from hohotree_be.api.views import ActivateUserView

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("plant-disease/", include("hohotree_be.plant_disease.urls")),
    # path("auth/", include("hohotree_be.auth.urls")),
    # path("user/", include("hohotree_be.user.urls")),
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/<str:uidb64>/<str:token>/', ActivateUserView.as_view(), name='activate'),
]