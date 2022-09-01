from django.urls import path
from dob import views

urlpatterns = [
    path("", views.LoginView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path("wishes/", views.WishesView.as_view()),
    path("song/", views.SongView.as_view()),
    path("memories/", views.MemoriesView.as_view()),
]