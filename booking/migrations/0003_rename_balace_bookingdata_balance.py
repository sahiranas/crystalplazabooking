# Generated by Django 3.2.5 on 2021-07-26 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_bookingdata_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingdata',
            old_name='balace',
            new_name='balance',
        ),
    ]
