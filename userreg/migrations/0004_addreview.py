# Generated by Django 4.2.5 on 2023-10-27 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userreg', '0003_userregistration_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ureview', models.CharField(max_length=100)),
            ],
        ),
    ]
