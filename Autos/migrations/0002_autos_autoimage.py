# Generated by Django 2.2.6 on 2020-03-18 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autos',
            name='autoImage',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Otomobilin Resmini Ekleyin'),
        ),
    ]
