# Generated by Django 2.1.7 on 2019-03-11 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64)),
                ('headline', models.CharField(max_length=64)),
                ('category', models.CharField(max_length=64)),
                ('region', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=64)),
                ('date', models.CharField(max_length=64)),
                ('details', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
