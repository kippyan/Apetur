from django.urls import path
from . import views

urlpatterns = [
    # homepage
    path('', views.home),

    # log in
    path('login', views.login_user),

    # log out
    path('logout', views.logout_user),

    # sign up
    path('signup', views.signup_user),

    # browse
    path('browse', views.browse)
]
