from django.urls import path
from . import views

urlpatterns =[
    path('notes/', views.showlist),
    path('notes/<str:pk>', views.details),
]