# Generated by Django 2.1.4 on 2019-01-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler_app', '0004_auto_20190105_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='mylist',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
