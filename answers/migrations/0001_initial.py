# Generated by Django 5.0.4 on 2024-04-16 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('answer_text', models.TextField(verbose_name='Answer Text')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Is Correct?')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.question', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
                'db_table': 'answers',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['answer_id'], name='answers_answer__c6a47c_idx')],
            },
        ),
    ]
