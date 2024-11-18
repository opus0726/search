# Generated by Django 3.2 on 2022-01-23 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='book',  # 古いモデル名
            new_name='search_app',  # 新しいモデル名
        ),
    ]
