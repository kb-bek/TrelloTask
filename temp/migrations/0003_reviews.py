# Generated by Django 4.0.4 on 2022-05-15 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0002_employees_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, db_index=True, verbose_name='Отзыв')),
                ('full_name', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='ФИО')),
                ('image', models.ImageField(blank=True, upload_to='image/%Y/%m/%d', verbose_name='Фото')),
                ('position', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Должность')),
            ],
        ),
    ]
