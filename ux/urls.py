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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from prototyping import views
from prototyping.feeds import LatestNewsFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('feed/', LatestNewsFeed()),
    path('tag/<str:tag>/', views.index, name='index'),
    path('tag/<str:tag>/page/<int:pagenumber>/', views.index, name='index'),
    path('page/<int:pagenumber>/', views.index),
    path('publications/', views.allpublications),
    path('publications/page/<int:pagenumber>/', views.allpublications),
    path('compare/prototyping/', views.prototyping, name='prototyping'),
    path('tools/' , views.alltools),
    path('tools/<str:slug>/' , views.prototypingtool),
    path('publications/<str:slug>/' , views.publications),
    path('freebies/' , views.allresources),
    path('toolbox/', views.globaltools),
    path('toolbox/prototyping/', views.alltools),
    path('toolbox/<str:slug>/', views.toolboxtool),
    path('toolbox/visual-design/<str:category>/', views.alltoolsinbox),
    path('toolbox/ux-design/<str:category>/', views.alltoolsinbox),
    path('toolbox/web-design/<str:category>/', views.alltoolsinbox),
    path('toolbox/reality/<str:category>/', views.alltoolsinbox),
    path('toolbox/ai/<str:category>/', views.alltoolsinbox),
    path('toolbox/vui/<str:category>/', views.alltoolsinbox),
    path('toolbox/accessibility/<str:category>/', views.alltoolsinbox),
    path('toolbox/design-systems/<str:category>/', views.alltoolsinbox),
    path('conferences/', views.conferences),
    path('talks/', views.videos),
    path('books/', views.books),
    #path('blog/', views.blog),
    #path('blog/page<int:num>/', views.blog),
    #path('signup/', views.signup),
    path('activateyouraccount/', views.activateyouraccount),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path('accountactive/', views.accountactive),
    path('invalidlink/', views.invalidlink),
    path('about/', views.about),
    path('contact/' , views.contact_me),
    url(r'^search/', include('haystack.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
