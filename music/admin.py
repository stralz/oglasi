from django.contrib import admin
from . import models
from django.contrib.auth.models import User

class KategorijaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}

class KategorijaToOglasInline(admin.TabularInline):
    model=models.KategorijaToOglas
    extra=1

class OglasAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("ime_oglasa",)}
    exclude = ('vlasnik',)
    inlines = [KategorijaToOglasInline]

    def save_model(self, request, obj, form, change):
        obj.vlasnik = request.user
        obj.save()

admin.site.register(models.Oglas, OglasAdmin)
admin.site.register(models.Kategorija, KategorijaAdmin)