# Generated by Django 3.2.5 on 2021-08-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0015_auto_20210727_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdata',
            name='id_proof',
            field=models.ImageField(blank=True, null=True, upload_to='id/'),
        ),
        migrations.AddField(
            model_name='bookingdata',
            name='kitchen_team',
            field=models.CharField(blank=True, default='Not Provided', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bookingdata',
            name='kitchen_team_license',
            field=models.ImageField(blank=True, null=True, upload_to='cook_license/'),
        ),
    ]
