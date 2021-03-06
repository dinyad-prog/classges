# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-10 20:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('annee', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='cour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.DateField(max_length=30)),
                ('hd', models.CharField(max_length=30)),
                ('hf', models.CharField(max_length=30)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classges.classe')),
            ],
        ),
        migrations.CreateModel(
            name='matiere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classges.classe')),
            ],
        ),
        migrations.CreateModel(
            name='personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('date_de_naissance', models.DateField()),
                ('sexe', models.CharField(max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('pwd', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='etudiant',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='classges.personne')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classges.classe')),
            ],
            bases=('classges.personne',),
        ),
        migrations.CreateModel(
            name='prof',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='classges.personne')),
                ('classe', models.ManyToManyField(to='classges.classe')),
            ],
            bases=('classges.personne',),
        ),
        migrations.AddField(
            model_name='cour',
            name='matiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classges.matiere'),
        ),
        migrations.AddField(
            model_name='matiere',
            name='prof',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='classges.prof'),
        ),
        migrations.AddField(
            model_name='cour',
            name='prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classges.prof'),
        ),
    ]
