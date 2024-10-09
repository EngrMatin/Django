from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.homeview),
    # path('api/', views.homedata),
    
    path('', views.HomeView.as_view()),
    path('api/', views.HomeAPIView.as_view()),
]
