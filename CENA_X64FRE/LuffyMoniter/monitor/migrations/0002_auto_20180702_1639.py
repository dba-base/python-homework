# Generated by Django 2.0.6 on 2018-07-02 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='items',
        ),
        migrations.RemoveField(
            model_name='template',
            name='services',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='ServiceIndex',
        ),
        migrations.DeleteModel(
            name='Template',
        ),
    ]
