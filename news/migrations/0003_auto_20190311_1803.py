# Generated by Django 2.1.7 on 2019-03-11 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190311_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='password',
            new_name='name',
        ),
    ]
