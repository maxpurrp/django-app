# Generated by Django 4.2.2 on 2023-07-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0004_workouts_gym_image_workouts_swimming_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workouts_gym',
            name='image',
            field=models.ImageField(null=True, upload_to='main/static/images_gym'),
        ),
        migrations.AlterField(
            model_name='workouts_swimming',
            name='image',
            field=models.ImageField(null=True, upload_to='main/static/images_swim'),
        ),
        migrations.AlterField(
            model_name='workouts_swimming_pro',
            name='image',
            field=models.ImageField(null=True, upload_to='main/static/images_swim_pro'),
        ),
    ]
