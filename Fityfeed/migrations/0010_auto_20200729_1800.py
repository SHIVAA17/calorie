# Generated by Django 3.0.6 on 2020-07-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fityfeed', '0009_userfooditem_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfooditem',
            name='customer',
            field=models.ManyToManyField(blank=True, to='Fityfeed.Customer'),
        ),
    ]
