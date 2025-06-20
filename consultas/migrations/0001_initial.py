# Generated by Django 5.2 on 2025-05-26 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sintomas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('caracteristicas', models.TextField()),
                ('factores', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Apoyo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('tipos', models.CharField(max_length=100)),
                ('diagnostico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apoyos', to='consultas.diagnostico')),
            ],
        ),
        migrations.CreateModel(
            name='Intervencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('estrategia', models.TextField()),
                ('diagnostico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intervenciones', to='consultas.diagnostico')),
            ],
        ),
        migrations.AddField(
            model_name='diagnostico',
            name='sintomas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnosticos', to='consultas.sintomas'),
        ),
    ]
