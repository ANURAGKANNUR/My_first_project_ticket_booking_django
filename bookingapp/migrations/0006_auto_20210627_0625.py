# Generated by Django 3.2.4 on 2021-06-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0005_auto_20210627_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='nos',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='bus',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='bus',
            name='rem',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
    ]
