# Generated by Django 4.1.7 on 2023-03-13 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='main_ipg',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка'),
        ),
    ]
