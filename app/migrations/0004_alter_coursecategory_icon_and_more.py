# Generated by Django 4.2.1 on 2023-09-24 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_instructor_sociallinkstypes_sociallinks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecategory',
            name='icon',
            field=models.FileField(upload_to='images/icons/'),
        ),
        migrations.AlterField(
            model_name='sociallinkstypes',
            name='icon',
            field=models.FileField(upload_to='images/icons/'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/course_images/')),
                ('price', models.PositiveIntegerField()),
                ('duration', models.PositiveIntegerField()),
                ('start', models.DateTimeField()),
                ('main_description', models.TextField()),
                ('benefits_description', models.TextField()),
                ('finish_description', models.TextField()),
                ('mini_review', models.CharField(max_length=200)),
                ('discount_percentage', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='app.coursecategory')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to='app.instructor')),
            ],
        ),
    ]