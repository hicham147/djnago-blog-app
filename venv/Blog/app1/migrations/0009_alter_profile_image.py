# Generated by Django 3.2.11 on 2023-01-01 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://upload.wikimedia.org/wikipedia/commons/a/ac/Default_pfp.jpg', upload_to='profile_pics'),
        ),
    ]
