# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Inventario',
            },
        ),
        migrations.CreateModel(
            name='Precios',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('precio', models.DecimalField(max_digits=9, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Precio',
            },
        ),
        migrations.CreateModel(
            name='PreciosTienda',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('precios', models.ForeignKey(to='inventory.Precios')),
            ],
            options={
                'verbose_name': 'Precio en tienda',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=200)),
                ('fecharegistro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('cedulaJuridica', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Tienda',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('unidad', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Unidades de producto',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.ForeignKey(to='inventory.Tipo'),
        ),
        migrations.AddField(
            model_name='producto',
            name='usuarioregistro',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='preciostienda',
            name='tienda',
            field=models.ForeignKey(to='inventory.Tienda'),
        ),
        migrations.AddField(
            model_name='precios',
            name='idproducto',
            field=models.ForeignKey(to='inventory.Producto'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='producto',
            field=models.ForeignKey(to='inventory.Producto'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='tienda',
            field=models.ForeignKey(to='inventory.Tienda'),
        ),
    ]
