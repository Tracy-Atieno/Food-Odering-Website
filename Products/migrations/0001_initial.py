# Generated by Django 4.2.5 on 2023-10-26 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prouct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptitle', models.CharField(max_length=50)),
                ('pprice', models.IntegerField()),
                ('p_image', models.FileField(max_length=200, null=True, upload_to='products/')),
            ],
        ),
    ]