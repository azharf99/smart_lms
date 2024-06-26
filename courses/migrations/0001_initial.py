# Generated by Django 5.0.4 on 2024-04-16 12:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=255, verbose_name='Course Name')),
                ('course_description', models.TextField(verbose_name='Course Description')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category', verbose_name='Category')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Instructor')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
                'db_table': 'courses',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['course_id'], name='courses_course__bcfb55_idx')],
            },
        ),
    ]
