# Generated by Django 2.0.2 on 2018-08-29 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funding', '0005_auto_20180820_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundingSourceMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False, verbose_name='Approved by PI')),
                ('fundingsource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funding.FundingSource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='fundingsource',
            name='users',
            field=models.ManyToManyField(blank=True, through='funding.FundingSourceMembership', to=settings.AUTH_USER_MODEL),
        ),
    ]
