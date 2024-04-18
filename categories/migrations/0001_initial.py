# Generated by Django 5.0.4 on 2024-04-16 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100, verbose_name='Category Name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'categories',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['category_id'], name='categories_categor_7f9b63_idx')],
            },
        ),
    ]