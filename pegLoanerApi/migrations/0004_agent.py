# Generated by Django 3.1.3 on 2020-11-21 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegLoanerApi', '0003_auto_20201121_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
