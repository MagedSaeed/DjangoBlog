# Generated by Django 2.2 on 2019-09-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20190911_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
