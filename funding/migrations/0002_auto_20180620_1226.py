# Generated by Django 2.0.2 on 2018-06-20 12:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('funding', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fundingbody',
            options={'ordering': ('name',), 'verbose_name_plural': 'Project Funding Sources'},
        ),
        migrations.AddField(
            model_name='fundingbody',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fundingbody',
            name='description',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fundingbody',
            name='modified_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='fundingbody',
            name='name',
            field=models.CharField(default='', max_length=128, unique=True),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='fundingbody',
            table=None,
        ),
    ]
