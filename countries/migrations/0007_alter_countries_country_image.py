# Generated by Django 3.2.9 on 2022-01-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0006_alter_countries_country_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='country_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
