# Generated by Django 2.1.7 on 2019-03-11 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20190311_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='news.Author'),
        ),
        migrations.AlterField(
            model_name='story',
            name='key',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]