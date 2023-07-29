# Generated by Django 4.1.7 on 2023-03-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=200, verbose_name='Заголовок главной страницы')),
                ('main_text', models.TextField(verbose_name='О чем речь вообще, где мы?')),
                ('pub_date', models.DateTimeField(verbose_name='Дата последнего обновления')),
            ],
            options={
                'verbose_name': 'Главная страница',
                'verbose_name_plural': 'главные страницы',
            },
        ),
    ]