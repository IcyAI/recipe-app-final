# Generated by Django 4.2.14 on 2024-08-03 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='users'),
        ),
    ]
