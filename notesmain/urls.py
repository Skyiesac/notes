from django.urls import path
from . import views

urlpatterns =[
    path('notes/', views.showlist , name='gotonote'),
    path('notes/<str:pk>', views.details, name='nodetail'),
     path('notes/new/', views.create_note, name='create_note'),
    path('notes/edit/<str:pk>/', views.editnote, name='editnote'),  # URL for editing a note
    path('notes/<str:pk>/delete/', views.deletenote, name='deletenote'),
]