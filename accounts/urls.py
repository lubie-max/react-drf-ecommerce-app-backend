from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path('register/',RegisterView.as_view()),
   path('login/',UserLoginView.as_view()),
   path('logout/', UserLogout.as_view()),
   path('profile/', UserProfileView.as_view() ),
   path('varify-otp/', VarifyingEmailByOtp.as_view()),
   path('change-password/', ChangeUserPasswordView.as_view()),


]
