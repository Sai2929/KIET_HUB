# Generated by Django 3.0.7 on 2020-06-29 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200629_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='year',
            field=models.IntegerField(choices=[(1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')]),
        ),
    ]
