# Generated by Django 3.1.3 on 2020-11-22 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegLoanerApi', '0006_auto_20201122_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='coordinates',
            field=models.CharField(default='', max_length=100),
        ),
    ]