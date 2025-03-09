
from . import views
from django.urls import path, re_path

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]   