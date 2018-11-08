"""ux URL Configuration

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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from prototyping import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('page/<int:pagenumber>/', views.index),
    path('compare/prototyping/', views.prototyping, name='prototyping'),
    path('tools/' , views.alltools),
    path('tools/<str:slug>/' , views.prototypingtool),
    path('publications/<str:slug>/' , views.publications),
    path('freebies/' , views.allresources),
    #path('toolbox/<str:slug>/', views.toolboxtool),
    path('toolbox/visualdesign/<str:category>/', views.alltoolsinbox),
    #path('blog/', views.blog),
    #path('blog/page<int:num>/', views.blog),
    path('signup/', views.signup),
    path('about/', views.about),
    path('contact/' , views.contact_me),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
