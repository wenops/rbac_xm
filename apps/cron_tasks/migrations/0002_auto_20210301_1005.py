# Generated by Django 3.1.6 on 2021-03-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cron_tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cron_task',
            name='task_res',
            field=models.TextField(blank=True, null=True, verbose_name='任务结果'),
        ),
        migrations.AlterField(
            model_name='cron_task',
            name='task_connent',
            field=models.TextField(blank=True, null=True, verbose_name='任务内容'),
        ),
    ]