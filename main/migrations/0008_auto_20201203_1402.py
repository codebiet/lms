# Generated by Django 3.1.3 on 2020-12-03 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20201203_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='pdf',
            name='tags',
        ),
    ]