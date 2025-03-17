from django.urls import path
from hohotree_be.users.views import RegisterView
from hohotree_be.users.views import ActivateUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', ActivateUserView.as_view(), name='activate'),
    
]