"""testve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from myfirst import views
#from myfirst.views import UserView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import routers, serializers, viewsets

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from myfirst.views import UserView


#urlpatterns = [
#    path('admin/', admin.site.urls),
 #   path('', views.home, name ='home'),
 #   path('yourname/', views.registerform,name='user'),
    #path('userprofiles/', views.userprofiles,name='userprofiles')
#    path('userprofiles/', UserView.as_view(),name='userprofiles')
    #path('userprofiles/', views.userprofiles,name='userprofiles')


#]


# urlpatterns = [
# path('admin/', admin.site.urls),
# path('', views.home, name ='home'),
# #path('userprofiles/', ProfileList.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='userprofiles'),
# path('userprofiles/',UserView.as_view(),name='userprofiles'),#queryset=User.objects.all()),name='userprofiles'),
# path('yourname/', views.registerform,name='user'),
# path('accounts/', include('django.contrib.auth.urls')),
# path('terminal', views.terminal),
# ]

urlpatterns = [
path('admin/', admin.site.urls),
path('', views.home, name ='home'),
#path('userprofiles/', ProfileList.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='userprofiles'),
path('userprofiles/<int:pk>',UserView.as_view(),name='userprofiles'),#queryset=User.objects.all()),name='userprofiles'),
#path('userprofiles/<int:id>',views.user),
path('yourname/', views.registerform,name='user'),
path('accounts/', include('django.contrib.auth.urls')),
path('oplata/',views.qiwiplata),
path('qiwi/',views.qiwi),
path('createpriсe/',views.creatprices),
path(r'accounts/login/$', include('django.contrib.auth.urls'), name='login'),
path('success',views.qiwipass),
path('price/', views.priselist),
path('price/details/<slug:slug>',views.prisedetails,name='details'),
path('terminal/<slug:slug>', views.terminal),
path('price/details/oplata/<slug:slug>',views.oplata)
]

