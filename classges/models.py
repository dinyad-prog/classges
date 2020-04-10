# -*- coding: utf-8 -*-
from django.conf import settings

from django.db import models


class classe(models.Model):
	nom=models.CharField(max_length=30)
	annee=models.CharField(max_length=10)

	def __unicode__(self):
		return self.nom
	

class personne(models.Model):
	nom=models.CharField(max_length=30)
	prenom=models.CharField(max_length=30)
	date_de_naissance=models.DateField()
	sexe=models.CharField(max_length=1)
	email=models.EmailField()
	pwd=models.CharField(max_length=30)

	def __unicode__(self):
		return self.prenom+" "+self.nom

class prof(personne):
	classe=models.ManyToManyField(classe)

class etudiant(personne):
	classe=models.ForeignKey(classe)

class matiere(models.Model):
	nom=models.CharField(max_length=30)
	classe=models.ForeignKey(classe)
	prof=models.OneToOneField(prof)

	def __unicode__(self):
		return self.nom
	
class cour(models.Model):
	jour=models.DateField(max_length=30)
	hd=models.CharField(max_length=30)
	hf=models.CharField(max_length=30)
	matiere=models.ForeignKey(matiere)
	classe=models.ForeignKey(classe)
	prof=models.ForeignKey(prof)

	def __unicode__(self):
		return self.jour+" "+self.hd+"-"+self.hf





# Create your models here.
