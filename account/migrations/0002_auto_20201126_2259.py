# Generated by Django 3.1.3 on 2020-11-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='roll_no',
            field=models.CharField(max_length=11),
        ),
    ]
