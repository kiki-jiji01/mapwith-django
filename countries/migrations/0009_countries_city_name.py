# Generated by Django 3.2.9 on 2022-01-27 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0008_alter_countries_country_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries',
            name='city_name',
            field=models.CharField(default='Tokyo', max_length=50),
            preserve_default=False,
        ),
    ]