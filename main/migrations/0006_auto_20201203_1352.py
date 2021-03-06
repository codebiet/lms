# Generated by Django 3.1.3 on 2020-12-03 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201202_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issued_book',
            name='last_date',
            field=models.DateField(default=datetime.date(2021, 3, 3)),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='tags',
            field=models.ManyToManyField(default=None, null=True, to='main.Tag'),
        ),
    ]
