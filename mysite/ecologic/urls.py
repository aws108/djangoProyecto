"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ecologic import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    #url(r'^categoria$', views.ItemListView.as_view() ),
    #url(r'^producte$', views.ItemListView.as_view() ),
    #url(r'^comanda$', views.ItemListView.as_view(success_url="/producte") ),
]

"""
urlpatterns = [
	url(r'^$', views.ItemListView.as_view() ),
	url(r'^torn$', views.ItemCreateView.as_view(success_url="/list") ),
	url(r'^list$', views.ItemListView.as_view() ),
	url(r'^vota$', views.VotaView.as_view() ),
	url(r'^vota2/(?P<votacio>[0-9]{0,10})/', views.votaActionView ), # view feta amb "metode classic"
    url(r'^admin/', admin.site.urls ),     # view del sistema d'administracio automatic de Django
]
"""