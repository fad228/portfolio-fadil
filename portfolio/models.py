from django.db import models

class CV(models.Model):
    nom = models.CharField(max_length=100, default='Mon CV')
    fichier = models.FileField(upload_to='cv/')
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
