# Generated by Django 5.1.1 on 2024-10-08 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rohan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_cars',
            name='Image',
            field=models.ImageField(default='rohandjango/rohan/static/img  (2).webp', upload_to='rohan/'),
        ),
    ]