# Generated by Django 5.1.1 on 2024-10-29 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rohan', '0003_alter_my_cars_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_cars',
            name='backside_car',
            field=models.ImageField(default='rohandjango/rohan/static/img.jpg', upload_to='rohan/'),
        ),
        migrations.AddField(
            model_name='my_cars',
            name='inside_car',
            field=models.ImageField(default='rohandjango/rohan/static/img.jpg', upload_to='rohan/'),
        ),
    ]