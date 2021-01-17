# Generated by Django 3.0.7 on 2020-06-29 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_leadership_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='branch',
            field=models.CharField(choices=[('', '-----'), ('ECE', 'Electronics & Communication Engineering'), ('CSE', 'Computer Science Engineering'), ('MECH', 'Mechanical Engineering'), ('CIV', 'Civil Engineering'), ('EEE', 'Electrical Engineering')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='college',
            field=models.CharField(choices=[('', '-----'), ('Kiet', 'Kiet'), ('Kiek', 'Kiet+'), ('Kietw', 'KietW')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='year',
            field=models.IntegerField(choices=[('', '-----'), (1, 'I'), (2, 'II'), (3, 'III'), (4, 'IV')], default=''),
        ),
    ]
