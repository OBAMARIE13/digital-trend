from django.db import models

# Create your models here.

class Banner(models.Model):
    image = models.FileField(upload_to='imageSite')
    libele = models.CharField(max_length = 200)
    titre = models.CharField(max_length = 200)
    numero = models.CharField(max_length = 200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.libele


class About(models.Model):
    titre = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.FileField(max_length = 200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.titre


class Temoignages(models.Model):
    photo = models.FileField(upload_to='imageSite')
    nom = models.CharField(max_length = 200)
    message = models.TextField()
    poste = models.CharField(max_length = 200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.nom


class Liens(models.Model):
    nom = models.CharField(max_length = 200)
    icone = models.CharField(max_length = 200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.nom

class Website(models.Model):
    nom_site = models.CharField(max_length = 200)
    titre_Temoignages = models.CharField(max_length = 200)
    nom_Futer = models.CharField(max_length = 200)
    contact = models.CharField(max_length = 200)
    mail = models.EmailField()
    adresse = models.CharField(max_length = 200)
    titre_Blog = models.CharField(max_length = 200)
    libelle_Newsletters = models.CharField(max_length = 200)
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.adresse


class Newsletters(models.Model):
    email = models.EmailField()
    date_add = models.DateTimeField(auto_now=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.email

