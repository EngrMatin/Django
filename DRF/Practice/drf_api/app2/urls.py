from django.urls import path
from .views import *

urlpatterns = [
    path('', secondAPI),
    path('reg/', registrationAPI),
    path('contact/', ContactAPIView.as_view()),
]