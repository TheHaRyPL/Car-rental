# Generated by Django 3.1.12 on 2021-06-22 10:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0005_auto_20210622_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='quantity',
        ),
        migrations.AddField(
            model_name='cars',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1)], verbose_name='Quantity'),
            preserve_default=False,
        ),
    ]