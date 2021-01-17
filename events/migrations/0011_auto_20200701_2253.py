# Generated by Django 3.0.7 on 2020-07-01 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0010_auto_20200701_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='editor',
            field=models.ForeignKey(default=models.SET('User'), null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
