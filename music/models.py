from django.contrib.auth.models import Permission, User
from django.db import models
from django.forms import HiddenInput, forms
from datetime import datetime
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    broj = models.CharField(max_length=15)
    slika = models.FileField(default='defprofilepic.png')
    lokacija = models.CharField(max_length=40)

    def __str__(self):
        return self.user.username

class Kategorija(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    description=models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Kategorije"

    def get_absolute_url(self):
        return "/kategorije/%s" % self.slug

class Oglas(models.Model):
    vlasnik = models.ForeignKey(User, default=1)
    ime_oglasa = models.CharField(max_length=500)
    slike = models.FileField()
    na_wishlist = models.BooleanField(default=False)
    datum_objave = models.DateTimeField(default=datetime.now, blank=True)
    opis=models.TextField(default='')
    grad=models.CharField(max_length=50, default='Sarajevo')
    cena=models.IntegerField(max_length=30, default=100)
    slug=models.SlugField(max_length=40, unique=True)
    kategorija = models.ForeignKey(Kategorija, default=1)
    KORISCENO = 'Korisceno'
    NOVO = 'Novo'
    STANJE_CHOICES = (
        (KORISCENO, 'Korisceno'),
        (NOVO, 'Novo'),
    )

    stanje = models.CharField(choices=STANJE_CHOICES, max_length=100, default=NOVO)
    def __str__(self):
        return self.ime_oglasa

    def get_absolute_url(self):
        return "/%s/%s/%s" %('music', 'oglasi', self.slug)

    class Meta:
        verbose_name_plural = "Oglasi"
        ordering = ["-datum_objave"]


class KategorijaToOglas(models.Model):
    oglas=models.ForeignKey(Oglas)
    kategorija=models.ForeignKey(Kategorija)