from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('', views.index, name='home'),
    path('logout/', views.logoutView, name='logout'),

]
