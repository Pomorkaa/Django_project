# Generated by Django 4.1.6 on 2023-07-29 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=500, verbose_name='Статус загрузки экскурсии')),
            ],
            options={
                'verbose_name': 'Статус загрузки экскурсии',
                'verbose_name_plural': 'Статусы загрузки экскурсии',
            },
        ),
        migrations.CreateModel(
            name='Trip_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500, verbose_name='Тип экскурсии')),
            ],
            options={
                'verbose_name': 'Тип экскурсии',
                'verbose_name_plural': 'Типы экскурсии',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Название')),
                ('number', models.CharField(max_length=50, verbose_name='Транспорт если есть')),
                ('seets', models.IntegerField(verbose_name='Количество мест')),
                ('children_seets', models.BooleanField(default=False, verbose_name='Детские места')),
                ('disabled_seets', models.BooleanField(default=False, verbose_name='Места для инвалидов')),
                ('time', models.CharField(max_length=400, verbose_name='Время экскурсии')),
                ('details', models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='Дополнительная информация')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Стоимость')),
                ('photo', models.ImageField(upload_to='', verbose_name='Рекламный баннер')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company', verbose_name='Компания')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.status', verbose_name='Статус')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.trip_type', verbose_name='Тип экскурси')),
            ],
            options={
                'verbose_name': 'Экскурсия',
                'verbose_name_plural': 'Экскурсия',
                'ordering': ['name'],
            },
        ),
    ]
