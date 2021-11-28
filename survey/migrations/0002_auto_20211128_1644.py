# Generated by Django 3.0 on 2021-11-28 14:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='age',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(120)]),
        ),
    ]
