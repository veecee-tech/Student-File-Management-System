# Generated by Django 3.2.8 on 2022-02-11 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='level',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(100, '100'), (200, '200'), (300, '300'), (400, '400'), (500, '500')], null=True),
        ),
    ]