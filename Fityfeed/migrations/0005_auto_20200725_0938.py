# Generated by Django 3.0.6 on 2020-07-25 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fityfeed', '0004_auto_20200725_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
