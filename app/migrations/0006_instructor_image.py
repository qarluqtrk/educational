# Generated by Django 4.2.1 on 2023-09-24 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_coursecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='image',
            field=models.FileField(default=django.utils.timezone.now, upload_to='images/instructors/'),
            preserve_default=False,
        ),
    ]
