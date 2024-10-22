from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

urlpatterns = [
      path('', views.getData),
      path('add/', views.addData),
      path('note/<int:id>',views.detailData),
      path('register/', views.RegisterView.as_view(), name='toregister'),
      path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    ]

urlpatterns = format_suffix_patterns(urlpatterns)