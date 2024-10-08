"""
URL configuration for cv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from my_cv import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.home),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("resume/", views.resume, name="resume"),
    path("services/", views.services, name="services"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("portfolio/estate-manage/", views.estate_manage, name="estate-manage"),
    path("portfolio/banking/", views.banking, name="banking"),
    path("portfolio/mini-calculator/", views.calculator, name="calc"),
    path("portfolio/tic-tac-toe/", views.tic_tac_toe, name="tic"),
    path("contact-me/", views.contact_me, name="contact-me"),
]
