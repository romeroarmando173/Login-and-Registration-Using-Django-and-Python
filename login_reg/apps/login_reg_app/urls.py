from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^addquote$', views.addquote),
    url(r'^addquote$', views.addquote),
    url(r'^posterPage/(?P<user_id>\d+)$', views.posterPage),
    url(r'^myAccount/(?P<user_id>\d+)$', views.myAccount),
    url(r'^UpdateDB1/(?P<user_id>\d+)$', views.UpdateDB1),
    url(r'^delete/(?P<quote_id>\d+)$', views.delete),  


]



