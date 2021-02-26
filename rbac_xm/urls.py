"""rbac_xm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


from system.views_user import IndexView,LoginView,LoginOutView
from system.views_manager import ManagerStu,StudentListView,StudentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LoginOutView.as_view(),name='logout'),
    path('system/',include('system.urls', namespace='system')),

    #任务管理系统
    path('cron_tasks/',include('cron_tasks.urls', namespace='cron_tasks')),

    path('manager/',ManagerStu.as_view(),name='student'),
    path('manager/stu/',StudentView.as_view(),name='stu'),
    path('manager/stu/list',StudentListView.as_view(),name='stu-list'),
]

from django.conf import settings
from django.urls import re_path
from django.views.static import serve

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),

    ]