"""
URL configuration for ArtyProd project.

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
from django import views
from django.contrib import admin
from django.urls import path
app_name = 'artyprod'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # Portfolio
    path('portfolio/', views.portfolio_list, name='portfolio_list'),
    path('portfolio/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),

    # Services
    path('services/', views.services_list, name='services_list'),
    path('services/<int:pk>/', views.services_detail, name='services_detail'),

    # Team
    path('team/', views.team_list, name='team_list'),
    path('team/<int:pk>/', views.team_detail, name='team_detail'),

    # Contact
    path('contact/', views.contact, name='contact'),
]
