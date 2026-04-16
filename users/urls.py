from django.urls import path
from .views import RegisterAPIView, ConfirmAPIView
from rest_framework_simplejwt.views import TokenObtainPairView 

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('confirm/', ConfirmAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
]