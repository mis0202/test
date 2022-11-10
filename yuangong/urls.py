"""yuangong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from yuangong1 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 部门管理
    path('depart/list/', views.depart_list),
    path('depart/add/', views.depart_add),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:nid>/edit/', views.depart_edit),

    # 用户管理
    path('user/list/', views.user_list),
    path('user/edit/', views.user_edit),
    path('user/delete/', views.user_delete),
    path('user/add/', views.user_add),
    path('user/<int:nid>/edit/', views.user_edit),

    # 靓号管理
    path('phone/list/', views.phone_list),
    path('phone/add/', views.phone_add),
    path('phone/<int:nid>/edit/', views.phone_edit),
    path('phone/delete/', views.phone_delete),

    # 设备类型
    path('dev/list/', views.dev_type_list),
    path('dev/<int:nid>/edit/', views.dev_edit),
]
