# Generated by Django 3.2.5 on 2021-07-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdata',
            name='post',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
