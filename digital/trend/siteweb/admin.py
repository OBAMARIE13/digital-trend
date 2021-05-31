from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("image", "libele", "titre", "numero", "date_add", "date_update", "status")


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("titre", "description", "image", "date_add", "date_update", "status")


@admin.register(models.Temoignages)
class Temoignages(admin.ModelAdmin):
    list_display = ("photo", "nom", "message", "poste", "date_add", "date_update", "status")


@admin.register(models.Liens)
class Liens(admin.ModelAdmin):
    list_display = ("nom", "icone", "date_add", "date_update", "status")

@admin.register(models.Newsletters)
class Newsletters(admin.ModelAdmin):
    list_display = ("email", "date_add", "date_update", "status")

@admin.register(models.Website)
class Website(admin.ModelAdmin):
    list_display = ("nom_site", "titre_Temoignages", "nom_Futer", "contact", "mail", "adresse", "titre_Blog", "libelle_Newsletters", "date_add", "date_update", "status")