"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from payments_app import views as payv
# from products_app import views as prov
# from review_app import views as revv

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', payv.django),
    # path('pro/', prov.cake),
    # path('rev/', revv.customer),
    path('', include('greetings_app.urls')),
    path('pay/', include('payments_app.urls')),
    path('pro/', include('products_app.urls')),
    path('rev/', include('review_app.urls')),
    
    
]
