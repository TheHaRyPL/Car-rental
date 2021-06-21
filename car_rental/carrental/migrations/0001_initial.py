# Generated by Django 3.1.12 on 2021-06-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('slug', models.SlugField(editable=False, max_length=256, unique=True)),
                ('mark', models.TextField(blank=True, null=True, verbose_name='Mark')),
                ('power', models.TextField(blank=True, null=True, verbose_name='Power')),
                ('type', models.TextField(blank=True, null=True, verbose_name='Type')),
                ('picture', models.ImageField(blank=True, null=True, verbose_name='Picture')),
            ],
        ),
    ]
