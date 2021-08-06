# Generated by Django 3.2.5 on 2021-07-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('house_name', models.CharField(max_length=255)),
                ('post', models.CharField(max_length=255, null=True)),
                ('location', models.CharField(max_length=255)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('advance', models.IntegerField()),
                ('total_amount', models.IntegerField(default=40000)),
                ('balace', models.IntegerField()),
                ('contact1', models.IntegerField()),
                ('contact2', models.IntegerField()),
            ],
        ),
    ]
