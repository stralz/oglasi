from django.conf.urls import url
from . import views

from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from django.views.generic import ListView
from music.models import Kategorija, Oglas

app_name = 'music'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #home page
    url(r'^$', views.index, name='index'),
    url(r'^(?P<selected_page>\d+)/?$', views.index, name='index_page'),
    url(r'^oglasi/(?P<slug>\w+)?$', views.DetailView.as_view(), name='detail'),
    url(r'^oglasi/(?P<slug>\w+)/wishlist_oglas/?$', views.wishlist_oglas, name='wishlist_oglas'),
    url(r'^oglasi/(?P<slug>\w+)/izbrisi_oglas/?$', views.Izbrisi_oglas.as_view(), name='izbrisi_oglas'),

    url(r'^kategorije/?$', ListView.as_view(
        model=Kategorija), name="list_kategorija"),
    url(r'^kategorije/(?P<kategorijaTitle>\w+)/?$', views.getKategorija, name='get_Kategorija'),
    url(r'^kategorije/(?P<kategorijaSlug>\w+)/(?P<selected_page>\d+)/?$', views.getKategorija, name='page_Kategorija'),


    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<oglas_id>[0-9]+)/$', views.getOglas, name='detailid'),
    url(r'^napravi_oglas/$', views.napravi_oglas, name='napravi_oglas'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile, name='get_user_profile'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/oglasi/$', views.oglasi_korisnik, name='oglasi_korisnik'),
]
