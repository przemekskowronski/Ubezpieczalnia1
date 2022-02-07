# Generated by Django 3.2.9 on 2022-02-06 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubezpieczenia', '0007_alter_dodatkoweinfo_gatunek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dodatkoweinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Elektronika'), (1, 'Samochód'), (0, 'Inne'), (3, 'Zdrowotne'), (2, 'Dom')], default=0),
        ),
    ]