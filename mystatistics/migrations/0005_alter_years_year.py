# Generated by Django 3.2.5 on 2021-08-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystatistics', '0004_rename_year_years_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='years',
            name='year',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]
