from django.urls import path
from dob import views

urlpatterns = [
    path("login/", views.LoginView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path("wishes/", views.WishesView.as_view()),
]