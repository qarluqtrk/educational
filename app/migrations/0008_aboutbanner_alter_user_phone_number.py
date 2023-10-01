# Generated by Django 4.2.1 on 2023-09-25 05:27

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_coursecategory_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/banner/')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=25, null=True, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^-?\\d+\\Z'), code='invalid', message='Enter a valid integer.')]),
        ),
    ]
