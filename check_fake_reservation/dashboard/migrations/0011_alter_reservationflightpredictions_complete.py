# Generated by Django 4.1.7 on 2023-05-09 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_rename_nbr_seat_reservationflight_number_of_chairs_to_reserve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationflightpredictions',
            name='complete',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
