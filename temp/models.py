from django.db import models


class Employees(models.Model):

    full_name = models.CharField(
        max_length=255,
        db_index=True,
        blank=True,
        verbose_name='ФИО')

    position = models.CharField(
        max_length=255,
        db_index=True,
        blank=True,
        verbose_name = 'Должность'
    )

    image = models.ImageField(
        upload_to='image/%Y/%m/%d',
        blank=True,
        verbose_name='Фото'
    )

    about = models.TextField(
        db_index=True,
        blank=True,
        verbose_name='Инфо'
    )


class Reviews(models.Model):

    review = models.TextField(
        db_index=True,
        blank=True,
        verbose_name='Отзыв'
    )

    full_name = models.CharField(
        max_length=255,
        db_index=True,
        blank=True,
        verbose_name='ФИО'
    )

    image = models.ImageField(
        upload_to='image/%Y/%m/%d',
        blank=True,
        verbose_name='Фото'
    )

    position = models.CharField(
        max_length=255,
        db_index=True,
        blank=True,
        verbose_name='Должность'
    )


