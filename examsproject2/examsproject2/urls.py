"""examsproject2 URL Configuration

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
from examapp2 import views
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base1/', views.base1),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view),
    path('first/', views.first_view),
    path('thanks/', views.thanks_view),
    path('Sixthquestion/', views.Sixthquestion),
    path('Seventhquestion/', views.Seventhquestion),
    path('Eigthquestion/', views.Eigthquestion),
    path('Ninthquestion/', views.Ninthquestion),
    path('Totalmarks/', views.TotalMarks),
    path('user_login/', views.user_login),
    path('dashboard/', views.Dashboard),
    url(r'^validate/(?P<id>\d+)/$', views.Validate),
    path('export/', views.Export),
    path('quit/', views.Quit),
    path('thanks/', views.Thanks),

]
