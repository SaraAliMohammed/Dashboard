"""DataCenterProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', 'blogs.views.dataCenterView', name='dataCenter'),
    url(r'^ajax/servers', 'blogs.views.servers_view', name='servers'),
    #url(r'^ajax/servers/add/$', 'blogs.views.addServerView'),

    url(r'^$', 'blogs.views.indexView', name='newIndex'),
    url(r'^new$', 'blogs.views.ServerCreateView', name='server_new'),
    url(r'^edit/(?P<pk>[\w ]+)$', 'blogs.views.ServerUpdateView', name='server_edit'),
    url(r'^delete/(?P<pk>[\w ]+)$', 'blogs.views.ServerDeleteView', name='server_delete'),

    url(r'^macs$', 'blogs.views.MacListView', name='mac_list'),
    url(r'^newMac$', 'blogs.views.AddMacToServerView', name='mac_new'),
    url(r'^editMac/(?P<pk>[\w ]+)$', 'blogs.views.UpdateMacView', name='mac_edit'),
    url(r'^showServerMacs/(?P<pk>[\w ]+)$', 'blogs.views.ShowServerMacsView', name='showServerMacs'),
    url(r'^showRacServers$', 'blogs.views.ShowRackServersView', name='showRacServers'),
    url(r'^index$', 'blogs.views.oldIndexView', name='index'),
    url(r'^oldIndex$', 'blogs.views.ServerListView', name='server_list'),
    url(r'^test$', 'blogs.views.test', name='test'),
    url(r'^serverDetails/(?P<pk>[\w ]+)$', 'blogs.views.ServerDetailsView', name='server_details'),

]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
