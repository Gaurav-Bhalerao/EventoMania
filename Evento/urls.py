from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.index,name = "home"),
    path("about/",views.about,name = "about"),
    path("portfolio/",views.portfolio,name = "portfolio"),
    path("contact/",views.contact,name = "contact"),
    path("register/",views.register,name = "register"),
    path("loginhandel/",views.loginhandel,name="loginhandel"),
    path("logouthandel/",views.logouthandel,name="logouthandel"),
]
