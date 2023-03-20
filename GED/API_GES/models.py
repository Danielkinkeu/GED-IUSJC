from django.db import models

# Create your models here.
class Categories(models.Model):
    code_categorie = models.CharField(max_length=50, default ='')
    nom_categorie  = models.CharField(max_length = 30)
    type_doc= models.CharField(max_length = 30)
    
    
    
class Historique(models.Model):
    id_document = models.CharField(max_length=50, default=" ")
    nom_doc_h  = models.CharField(max_length=50, default=" ")
    
    
  
    
class Documents(models.Model):
    id_doc = models.CharField(max_length=50, default=" ")
    nom_doc  = models.CharField(max_length=50, default=" ")
    date_creation = models.DateField()
    date_archivage = models.DateField()
    traitement = models.CharField(max_length=50, default=" ")
    type_doc = models.CharField(max_length=50, default=" ")
    nom_modifieur = models.CharField(max_length=50, default=" ")
    date_creation_doc = models.DateField()
    description_doc = models.CharField(max_length=50, default=" ")
    
   
    
class Visibilite(models.Model):
    # id_doc = models.CharField(max_length=50, default=" ")
    code_utilisateur  = models.CharField(max_length = 30,  default = '')
    
   