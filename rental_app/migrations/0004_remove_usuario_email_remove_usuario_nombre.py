# Generated by Django 5.1 on 2025-01-31 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0003_equipo_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
    ]
