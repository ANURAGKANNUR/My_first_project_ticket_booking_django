# Generated by Django 3.2.4 on 2021-06-27 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0006_auto_20210627_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bus_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]