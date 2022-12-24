from django.urls import path
from user.views import UserSignUpView

urlpatterns = [
    path('', UserSignUpView.as_view()),
    path('login', UserSignUpView.as_view()),
]