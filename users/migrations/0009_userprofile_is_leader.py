# Generated by Django 3.0.7 on 2020-06-30 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200630_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_leader',
            field=models.BooleanField(default=False),
        ),
    ]
