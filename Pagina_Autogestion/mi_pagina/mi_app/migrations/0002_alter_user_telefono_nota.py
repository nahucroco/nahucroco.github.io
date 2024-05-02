# Generated by Django 5.0.3 on 2024-04-15 23:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telefono',
            field=models.CharField(max_length=25),
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.user')),
            ],
        ),
    ]
