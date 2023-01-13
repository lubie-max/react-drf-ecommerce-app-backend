from django.urls import path
from .views import *


urlpatterns = [
    path('',ProductView.as_view()),
    path('categories/',CategoryView.as_view()),
    path('cart/', CartView.as_view()) ,

]
