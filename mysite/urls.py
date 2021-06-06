"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from poll.views import polls_list, polls_list_u, poll_details, names_list, form_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('pollslist/', polls_list),
    path('pollslist2/', polls_list_u),
    path('polldetails/<str:p_title>', poll_details), 
    path('nameslist/', names_list),
    path('form/', form_list),
    
]
