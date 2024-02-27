"""
URL configuration for E_commers project.

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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/social-media/', views.social_media, name='social_media_dashboard'),
    path('products/ar/', views.ar_home, name='ar_home'),
    path('products/', views.product_list, name='product_list'),
    path('products/cart/', views.view_cart, name='view_cart'),
    path('products/chat/<str:room_name>/', views.chat_room, name='chat_room'),
]

