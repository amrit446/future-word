from django.contrib import admin
from django.urls import path
from home import views
from home import views1
urlpatterns = [
    
    path("", views.index, name='home'),
    path("login", views1.loginuser, name='login'),
    path("signup", views.signup, name='signup'),
    path("userdetail", views.userdetail, name='userdetail'),
    path('delete/<int:id>/', views.del_data, name='deletedata'),
    path('<int:id>/', views.update_data, name='updatedata'),
    
]
