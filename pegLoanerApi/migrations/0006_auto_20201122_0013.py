# Generated by Django 3.1.3 on 2020-11-22 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegLoanerApi', '0005_customer_agent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='realPaidAmount',
            new_name='repaidAmount',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='lastName',
        ),
        migrations.AddField(
            model_name='agent',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='000000000000', max_length=20),
        ),
    ]