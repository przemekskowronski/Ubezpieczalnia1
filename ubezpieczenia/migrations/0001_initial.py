# Generated by Django 3.2.9 on 2022-01-31 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ubezpieczenie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=64)),
                ('opis', models.TextField(default='')),
                ('premiera', models.DateField(blank=True, null=True)),
                ('znizka', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('plakat', models.ImageField(blank=True, null=True, upload_to='plakaty')),
            ],
        ),
    ]
