# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import etudiant,classe,prof,matiere,cour
# Register your models here.

admin.site.register(etudiant)
admin.site.register(classe)
admin.site.register(prof)
admin.site.register(matiere)
admin.site.register(cour)