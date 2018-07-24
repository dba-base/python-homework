# Generated by Django 2.0.6 on 2018-06-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='服务名称')),
                ('interval', models.IntegerField(default=60, verbose_name='监控间隔')),
                ('plugin_name', models.CharField(default='n/a', max_length=64, verbose_name='插件名')),
                ('has_sub_service', models.BooleanField(default=False, help_text='如果一个服务还有独立的子服务 ,选择这个,比如 网卡服务有多个独立的子网卡')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('key', models.CharField(max_length=64, unique=True)),
                ('data_type', models.CharField(choices=[('int', 'int'), ('float', 'float'), ('str', 'string')], default='int', max_length=32, verbose_name='指标数据类型')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='模版名称')),
                ('services', models.ManyToManyField(to='monitor.Service', verbose_name='服务列表')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='items',
            field=models.ManyToManyField(blank=True, to='monitor.ServiceIndex', verbose_name='指标列表'),
        ),
    ]
