from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<oglas_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^napravi_oglas/$', views.napravi_oglas, name='napravi_oglas'),
    url(r'^(?P<oglas_id>[0-9]+)/wishlist_oglas/$', views.wishlist_oglas, name='wishlist_olgas'),
    url(r'^(?P<oglas_id>[0-9]+)/izbrisi_oglas/$', views.izbrisi_oglas, name='izbrisi_oglas'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile),

]
