from django.urls import path
from ..users.views import RegisterView
from hohotree_be.users.views import ActivateUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/<str:uidb64>/<str:token>/', ActivateUserView.as_view(), name='activate'),
    
]