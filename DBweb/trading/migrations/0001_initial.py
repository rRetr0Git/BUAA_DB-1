# Generated by Django 2.1.2 on 2018-11-17 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('account', models.CharField(max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('credit', models.IntegerField()),
                ('mobile_number', models.IntegerField()),
                ('address', models.CharField(max_length=256)),
                ('img_src', models.CharField(max_length=256)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '用户',
                'verbose_name': '用户',
                'ordering': ['c_time'],
            },
        ),
    ]
