# Generated by Django 2.0.6 on 2018-06-22 02:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='业务系统')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='厂商')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=64, verbose_name='主机名')),
                ('instance_name', models.CharField(max_length=64, verbose_name='实例名')),
                ('ip_addr', models.GenericIPAddressField(unique=True, verbose_name='IP地址')),
                ('port', models.PositiveSmallIntegerField(default=22, verbose_name='端口号')),
                ('username', models.CharField(max_length=64, verbose_name='用户名')),
                ('db_username', models.CharField(max_length=64)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('db_password', models.CharField(blank=True, max_length=128, null=True)),
                ('database_type', models.SmallIntegerField(choices=[(0, 'oracle 10g'), (1, 'oracle 11g'), (2, 'oracle 12c'), (3, 'mysql')], default=0, verbose_name='数据库类型')),
                ('os_type', models.SmallIntegerField(choices=[(0, 'Linux'), (1, 'windows'), (2, 'AIX')], default=0, verbose_name='OS类型')),
                ('opatch_version', models.CharField(max_length=64, verbose_name='补丁')),
                ('enabled', models.BooleanField(default=True)),
                ('appcompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.AppCompany', verbose_name='厂商')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Business', verbose_name='业务系统名称')),
            ],
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='机房')),
            ],
        ),
        migrations.CreateModel(
            name='Tablespace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('total_size', models.CharField(blank=True, max_length=64)),
                ('free_size', models.CharField(blank=True, max_length=64)),
                ('used_size', models.CharField(blank=True, max_length=64)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日期')),
                ('host', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.Host')),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.IDC', verbose_name='机房'),
        ),
    ]
