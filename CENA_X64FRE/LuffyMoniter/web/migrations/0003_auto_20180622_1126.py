# Generated by Django 2.0.6 on 2018-06-22 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180622_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablespace',
            name='time',
            field=models.TimeField(auto_now=True, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='tablespace',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='日期'),
        ),
    ]
