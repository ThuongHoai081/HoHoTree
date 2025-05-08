from django.urls import path
from src.users.views import RegisterView
from src.users.views import ActivateUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/<slug:token>/', ActivateUserView.as_view(), name='activate'), 
    
]