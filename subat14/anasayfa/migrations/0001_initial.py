# Generated by Django 3.2.12 on 2022-03-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ogr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim_soyad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ogr2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim_soyad', models.CharField(max_length=50)),
                ('aciklama', models.TextField(max_length=50)),
            ],
        ),
    ]
