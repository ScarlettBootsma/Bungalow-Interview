# Generated by Django 2.1.1 on 2018-09-04 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_auto_20180818_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='num_bathrooms',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
