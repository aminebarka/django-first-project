from django.db import models

class Projet(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

class Service(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

class Detail(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    fichier = models.FileField(upload_to='fichiers/')

class Personnel(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=255)

class Equipe(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    personnel = models.ManyToManyField(Personnel)
