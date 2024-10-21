from django.urls import path 
from home import views 

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logoutvi, name='logout'),
]
