# Generated by Django 5.0.4 on 2024-04-16 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_text', models.TextField(verbose_name='Question Text')),
                ('question_type', models.CharField(choices=[('multiple_choice', 'Multiple Choice'), ('short_answer', 'Short Answer'), ('true_false', 'True/False')], max_length=20, verbose_name='Answer Type')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz', verbose_name='Quiz')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
                'db_table': 'questions',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['question_id'], name='questions_questio_027876_idx')],
            },
        ),
    ]
