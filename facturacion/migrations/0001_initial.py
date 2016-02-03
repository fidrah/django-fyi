# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('cancelado', models.BooleanField(default=False)),
                ('producto', models.ForeignKey(to='inventory.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('cancelada', models.BooleanField(default=False)),
                ('fechacrecacion', models.DateTimeField(auto_now_add=True)),
                ('total', models.IntegerField()),
                ('detalle', models.CharField(max_length=200)),
                ('tienda', models.ForeignKey(to='inventory.Tienda')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FacturaDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('detalle', models.ForeignKey(to='facturacion.Detalle')),
                ('factura', models.ForeignKey(to='facturacion.Factura')),
            ],
        ),
        migrations.CreateModel(
            name='Reimpresion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('factura', models.ForeignKey(to='facturacion.Factura')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudCancelacion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('detalle', models.CharField(max_length=200)),
                ('aceptado', models.BooleanField(default=False)),
                ('admin', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='approver')),
                ('factura', models.ForeignKey(to='facturacion.Factura')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='requester')),
            ],
        ),
    ]
