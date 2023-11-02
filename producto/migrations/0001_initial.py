# Generated by Django 4.2.6 on 2023-10-31 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('usuario', models.TextField(max_length=50, null=True, verbose_name='Usuario')),
                ('correo', models.TextField(max_length=75, null=True, verbose_name='Correo')),
                ('descripcion', models.TextField(max_length=200, null=True, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=50, verbose_name='Nombre del producto')),
                ('descripcion', models.TextField(max_length=200, verbose_name='Descripcion del producto')),
                ('existencias', models.IntegerField(verbose_name='Existencias  del producto')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Precio del producto')),
            ],
        ),
    ]