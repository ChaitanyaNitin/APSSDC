"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Firstapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('he/',views.htmltag),
    path('usr/<str:uname>/',views.usernameprint),
    path('usag/<str:un>/<int:ag>/',views.usernameage),
    path('emp/<str:ename>/<int:eage>/<str:eid>/',views.empdetails),
    path('qw/',views.htm),
    path('yt/<str:name>/',views.ytname),
    path('pt/<int:id>/<str:ename>/',views.empname),
    path('stud/',views.studdets),
    path('internalJS/',views.internalJS),
    path('myform/',views.myform,name='myform'),
    path('register/',views.reg,name='register'),
    path('login/',views.log,name='login'),
    path('btstrp/',views.bootstrapfun),
    path('btreg/',views.btreg,name='btr'),
    path('register1/',views.register1),
    path('regis/',views.regis,name = "regis"),
    path('display/',views.display,name="dt"),
    path('view/<int:y>/',views.sview,name="sv"),
    path('update/<int:q>/',views.supdate,name="sup"),
    path('delete/<int:p>/',views.sdelete,name="sd"),
]
