from django.contrib.auth.models import Permission, User
from django.db import models
from django.forms import HiddenInput, forms


class Oglas(models.Model):
    vlasnik = models.ForeignKey(User, default=1)
    ime_oglasa = models.CharField(max_length=500)
    slike = models.FileField()
    na_wishlist = models.BooleanField(default=False)

    def __str__(self):
        return self.ime_oglasa