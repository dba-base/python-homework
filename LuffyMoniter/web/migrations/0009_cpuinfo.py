# Generated by Django 2.0.6 on 2018-07-04 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_host_templates'),
    ]

    operations = [
        migrations.CreateModel(
            name='CpuInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]