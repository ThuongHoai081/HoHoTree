# from django.contrib import admin
# from django.urls import path, include

# from rest_framework import permissions
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# urlpatterns = [
#     # path("admin/", admin.site.urls),
#     path("plant-disease/", include("hohotree_be.plant_disease.urls")),
#     path("auth/", include("hohotree_be.users.urls")),
#     path("auth/login/", TokenObtainPairView.as_view(), name="login"),
#     path("auth/refresh-token/", TokenRefreshView.as_view(), name="refresh_token"),
# ]

from django.urls import path, include
from hohotree_be.plant_disease.views import predict_image

from hohotree_be.users.views import RegisterView, ActivateUserView, SupabaseLoginView, SupabaseRefreshTokenView

urlpatterns = [
    path("plant-disease/", include("hohotree_be.plant_disease.urls")),

    # Supabase Auth
    path("auth/", include("hohotree_be.users.urls")),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/activate/<slug:token>/", ActivateUserView.as_view(), name="activate"),
    path("auth/login/", SupabaseLoginView.as_view(), name="login"),
    path("auth/refresh-token/", SupabaseRefreshTokenView.as_view(), name="refresh_token"),
    path("plant/", predict_image),
]
