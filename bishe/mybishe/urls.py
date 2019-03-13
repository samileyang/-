"""bishe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from mybishe import views
from django.conf.urls import url
urlpatterns = [
    url(r'^stu_info/',views.stu_info),
    url(r'^stu_index/',views.stu_index),
    url(r'^stu_login/',views.stu_login),
    url(r'^jwc_index/',views.jwc_index),
]
