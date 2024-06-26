# Generated by Django 5.0.3 on 2024-04-15 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreApellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60)),
                ('telefono', models.CharField(blank=True, max_length=25, null=True)),
                ('usuario', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
