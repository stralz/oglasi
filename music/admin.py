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

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from music.models import Employee

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


admin.site.register(models.Oglas, OglasAdmin)
admin.site.register(models.Kategorija, KategorijaAdmin)