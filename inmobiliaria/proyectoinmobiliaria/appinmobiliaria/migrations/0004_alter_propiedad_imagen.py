# Generated by Django 5.1 on 2024-08-24 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinmobiliaria', '0003_alter_propiedad_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='imagen',
            field=models.ImageField(upload_to='imagenes/'),
        ),
    ]