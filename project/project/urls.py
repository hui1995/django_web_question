"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from userApp import views
from myApp import views as views2

urlpatterns = [
    path('login/', views.AuthLogin.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('logout/', views.LoginOut.as_view()),
    path('admin/',views2.adminView.as_view()),
    path('index/',views2.IndexView.as_view()),
    path('answer/',views2.IndexAnsView.as_view()),
    path('detail/',views2.adminDetailView.as_view()),
    path('end/',views2.endView.as_view()),
    path('user/list/',views2.adminUserListView.as_view()),
    path('user/detail/',views2.adminUserLisDetailtView.as_view()),
]
