# Generated by Django 4.2.5 on 2023-10-27 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userreg', '0002_bannerdesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='Image',
            field=models.ImageField(null=True, upload_to='profile/'),
        ),
    ]
