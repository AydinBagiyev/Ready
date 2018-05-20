from django.conf.urls import url

from webapp import views


urlpatterns = [
    url(r'^cats/$', views.CatList.as_view(), name='cat_list'),
    url(r'^cats/(?P<pk>[0-9]+)$', views.CatDetail.as_view(), name='cat_detail'),
    url(r'^dogs/$', views.DogList.as_view(), name='dog_list'),
    url(r'^dogs/(?P<pk>[0-9]+)$', views.DogDetail.as_view(), name='dog_detail'),
]
