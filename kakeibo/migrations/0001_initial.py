# Generated by Django 2.0.6 on 2019-09-10 16:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Kakeibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='日付')),
                ('money', models.IntegerField(help_text='単位は日本円', verbose_name='金額')),
                ('memo', models.CharField(max_length=500, verbose_name='メモ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kakeibo.Category', verbose_name='カテゴリ')),
            ],
            options={
                'db_table': 'kakeibo',
            },
        ),
    ]
