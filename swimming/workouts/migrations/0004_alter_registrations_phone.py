# Generated by Django 4.2.2 on 2023-06-29 20:38

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_registrations_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrations',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
