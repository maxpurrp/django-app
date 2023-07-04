# Generated by Django 4.2.2 on 2023-07-04 19:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_registrations_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouts_gym',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images_gym'),
        ),
        migrations.AddField(
            model_name='workouts_swimming',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images_swim'),
        ),
        migrations.AddField(
            model_name='workouts_swimming_pro',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images_swim_pro'),
        ),
        migrations.AlterField(
            model_name='registrations',
            name='phone',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must me entered in format : "89965592812', regex='^((8|\\+7)[\\- ]?)?(\\(?\\d{3}\\)?[\\- ]?)?[\\d\\- ]{7,10}$')]),
        ),
    ]