# Generated by Django 3.1.12 on 2021-06-22 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrental', '0007_auto_20210622_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='mark',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mark'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='power',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Power'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='price',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Type'),
        ),
    ]