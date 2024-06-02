from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

]
