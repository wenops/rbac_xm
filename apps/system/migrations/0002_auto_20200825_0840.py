# Generated by Django 2.1.2 on 2020-08-25 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['number'], 'verbose_name': '菜单', 'verbose_name_plural': '菜单'},
        ),
        migrations.AddField(
            model_name='menu',
            name='number',
            field=models.FloatField(blank=True, null=True, verbose_name='编号'),
        ),
    ]
