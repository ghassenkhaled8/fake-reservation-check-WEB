# Generated by Django 4.1.7 on 2023-04-11 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_flight_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='flight_day_end',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='flight_day_start',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='flight_hour_end',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='flight_hour_start',
        ),
        migrations.AddField(
            model_name='flight',
            name='flight_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='flight',
            name='flight_start',
            field=models.DateTimeField(null=True),
        ),
    ]