# Generated by Django 2.1.7 on 2019-03-12 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20190311_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='region',
            field=models.CharField(choices=[('uk', 'UK'), ('eu', 'European'), ('w', 'World')], max_length=64),
        ),
    ]