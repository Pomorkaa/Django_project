# Generated by Django 4.1.6 on 2023-08-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_trip_decription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='decription',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
