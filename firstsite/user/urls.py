from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(), name='profile_edit'),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
