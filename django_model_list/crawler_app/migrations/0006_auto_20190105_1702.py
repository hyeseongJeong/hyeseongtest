# Generated by Django 2.1.4 on 2019-01-05 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler_app', '0005_auto_20190105_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='mylist',
            field=models.CharField(max_length=200),
        ),
    ]
