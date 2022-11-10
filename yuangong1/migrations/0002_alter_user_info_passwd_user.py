# Generated by Django 4.1.2 on 2022-10-18 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yuangong1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='passwd',
            field=models.IntegerField(verbose_name='密码'),
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('passwd', models.IntegerField(verbose_name='密码')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('phone_num', models.IntegerField(verbose_name='手机号')),
                ('mail', models.CharField(max_length=132, verbose_name='邮箱地址')),
                ('create_time', models.DateTimeField(verbose_name='入职时间')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yuangong1.department', verbose_name='部门ID')),
            ],
        ),
    ]