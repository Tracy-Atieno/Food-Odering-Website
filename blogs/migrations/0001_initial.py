# Generated by Django 4.2.5 on 2023-11-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('image', models.ImageField(default=None, max_length=250, null=True, upload_to='image/')),
                ('url', models.URLField(null=True)),
            ],
        ),
    ]
