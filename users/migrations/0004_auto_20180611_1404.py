# Generated by Django 2.0.2 on 2018-06-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180611_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='UID Number'),
        ),
    ]
