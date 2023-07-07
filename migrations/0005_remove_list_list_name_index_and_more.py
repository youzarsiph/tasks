# Generated by Django 4.2 on 2023-07-07 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_list_options_alter_task_options_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='list',
            name='list_name_index',
        ),
        migrations.RemoveIndex(
            model_name='task',
            name='task_title_index',
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, db_index=True, help_text='Task deadline', null=True),
        ),
    ]
