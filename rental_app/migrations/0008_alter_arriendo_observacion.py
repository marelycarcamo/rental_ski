# Generated by Django 5.1 on 2025-02-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0007_alter_arriendo_observacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arriendo',
            name='observacion',
            field=models.TextField(blank=True, default='Sin observaciones', null=True),
        ),
    ]
