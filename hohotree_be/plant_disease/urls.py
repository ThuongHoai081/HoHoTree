
from . import views
from django.urls import path, re_path

urlpatterns = [
    path(r'^hello-view/', views.HelloApiView.as_view()),
]   