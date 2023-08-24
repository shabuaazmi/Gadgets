"""
URL configuration for gadgets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from electronics import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('createac/',views.createac),
    path('createac1/',views.createac1),
    path('login1/',views.login1),
    path('adminpage/',views.adminpage),
    path('userpage/',views.userpage),
    path('userprofile/',views.userprofile1),
    path('updateprofile/<int:id>',views.updateprofile),
    path('updateprofile1/<int:id>',views.updateprofile1),
    path('gadget1/',views.gadget),
    path('addgadget1/',views.addgadget),
    path('gadgetsform/',views.gadgetform),
    path('gadgetsform1/',views.gadgetform1),
    path('viewgedget/',views.viewgedget),
    path('viewmobile/',views.viewmobile),
    path('less50000/',views.lessprice),
    path('usertable/',views.usertable),
    path('dltuser/<int:id>',views.dltuser),
    path('back_user/',views.userpage),
    path('back_admin/',views.adminpage),
    path('updategadget/<int:id>',views.updategadget),
    path('updategadget1/<int:id>',views.updategadget1),
    path('dltgadget/<int:id>',views.dltgadget),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)