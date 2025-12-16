from django.urls import path
from .api import LoginAPIView, LogoutAPIView , UserRegistrationView , DeleteAccountAPIView

urlpatterns = [
    path('api/login/', LoginAPIView.as_view()),
    path('api/logout/', LogoutAPIView.as_view()),
    path('api/register/',UserRegistrationView.as_view()),
    path("api/delete/" , DeleteAccountAPIView.as_view()),
]                       