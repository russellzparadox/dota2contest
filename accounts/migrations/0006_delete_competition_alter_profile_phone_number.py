# Generated by Django 4.2.3 on 2023-08-04 08:54

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_competition'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Competition',
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=12, validators=[accounts.models.validate_phone_number]),
        ),
    ]
