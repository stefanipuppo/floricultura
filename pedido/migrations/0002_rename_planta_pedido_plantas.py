# Generated by Django 5.0.7 on 2024-08-10 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='planta',
            new_name='plantas',
        ),
    ]
