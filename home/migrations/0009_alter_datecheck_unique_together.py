# Generated by Django 3.2.5 on 2021-07-30 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_datecheck_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='datecheck',
            unique_together=set(),
        ),
    ]
