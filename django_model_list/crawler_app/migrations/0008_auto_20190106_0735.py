# Generated by Django 2.1.4 on 2019-01-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler_app', '0007_auto_20190105_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
