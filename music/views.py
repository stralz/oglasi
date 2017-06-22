from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import OglasForm,  UserForm
from .models import Oglas, Kategorija
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.core.paginator import Paginator, EmptyPage
from django.template import RequestContext
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View


AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def napravi_oglas(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        form = OglasForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            oglas = form.save(commit=False)
            oglas.vlasnik = request.user
            oglas.slike = request.FILES['slike']
            file_type = oglas.slike.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'oglas': oglas,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'music/napravi_oglas.html', context)
            oglas.save()
            return render(request, 'music/detail.html', {'oglas': oglas})
        context = {
            "form": form,
        }
        return render(request, 'music/napravi_oglas.html', context)
"""
def izbrisi_oglas(request, id):
    oglas = Oglas.objects.get(pk=id)
    oglas.delete()
    oglasi = Oglas.objects.filter(vlasnik=request.user)
    return render_to_response('music/index.html', {'oglasi': oglasi}, RequestContext(request))
"""

class Izbrisi_oglas(DeleteView):
    model = Oglas
    success_url = reverse_lazy('music:index')


def detail(request, oglas_id):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        vlasnik = request.user
        oglas = get_object_or_404(Oglas, pk=oglas_id)
        return render(request, 'music/detail.html', {'oglasi': oglas, 'vlasnik': vlasnik})

def wishlist_oglas(request, oglas_id):
    oglas = get_object_or_404(Oglas, pk=oglas_id)
    try:
        if oglas.na_wishlist:
            oglas.na_wishlist = False
        else:
            oglas.na_wishlist = True
        oglas.save()
    except (KeyError, Oglas.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})

def index(request, selected_page=1):
    oglasi = Oglas.objects.all().order_by('-datum_objave')
    pages=Paginator(oglasi, 5)
    returned_page=pages.page(selected_page)

    try:
        returned_page=pages.page(selected_page)
    except EmptyPage:
        returned_page=pages.page(pages.num_pages)

    return render(request, 'music/index.html', { 'oglasi':returned_page.object_list , 'kategorije' : Kategorija.objects.all(), 'request' : request})

def getOglas(request, oglasSlug):
    oglas=Oglas.objects.filter(slug=oglasSlug)

    return render_to_response('music/single.html', { 'oglas': oglas}, context_instance=RequestContext(request))

def getKategorija(request, kategorijaSlug, selected_page=1):
    oglasi=Oglas.objects.all().order_by('-datum_objave')
    kategorija_oglasi=[]
    for oglas in oglasi:
        if oglas.kategorije.filter(slug=kategorijaSlug):
            kategorija_oglasi.append(oglas)

    pages=Paginator(kategorija_oglasi, 5)

    kategorija=Kategorija.objects.filter(slug=kategorijaSlug)[0]

    try:
        returned_page=pages.page(selected_page)
    except EmptyPage:
        returned_page=pages.page(pages.num_pages)

    return render_to_response('music/kategorija.html', {'oglasi' : returned_page.object_list, 'page':returned_page, 'kategorija' : kategorija})

class DetailView(generic.DetailView):
    model = Oglas
    template_name = 'music/detail.html'

"""
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
       
            return render(request, 'music/index.html', {
                'oglasi': oglasi,
            })
        else:
            return render(request, 'music/index.html', {'oglasi': oglasi})

"""
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                oglasi = Oglas.objects.filter(vlasnik=request.user)
                return render(request, 'music/index.html', {'oglasi': oglasi})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                oglasi = Oglas.objects.filter(vlasnik=request.user)
                return render(request, 'music/index.html', {'oglasi': oglasi})
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)


def faq(request):
    return render(request, 'music/faq.html')


def get_user_profile(request, username):
    user = User.objects.get(username=username)
    oglasi = Oglas.objects.filter(vlasnik=user)
    return render(request, 'music/user_profile.html', {'user': user, 'oglasi': oglasi, 'request': request})


def oglasi_korisnik(request, username):
    user = User.objects.get(username=username)
    oglasi = Oglas.objects.filter(vlasnik=user)
    return render(request, 'music/oglasi_korisnik.html', {"user":user, 'oglasi': oglasi, 'request': request})
