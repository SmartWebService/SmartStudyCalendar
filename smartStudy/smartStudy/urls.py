"""smartStudy URL Configuration

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
from django.urls import path, include
import everytime.views
import calendarapp.views
import accounts.views

urlpatterns = [
    path('', calendarapp.views.my),
    path('admin/', admin.site.urls),
    path('connect-everytime', everytime.views.connect_everytime),
    path('connect-everytime/post', everytime.views.post),
    path('connect-everytime/how-to', everytime.views.howto),
    path('login', accounts.views.login, name='login'),
    path('accounts/', include('allauth.urls')),
]
