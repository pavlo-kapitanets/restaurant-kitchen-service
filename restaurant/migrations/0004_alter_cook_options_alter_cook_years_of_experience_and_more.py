# Generated by Django 4.1.3 on 2022-12-05 16:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0003_alter_dish_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cook",
            options={
                "ordering": ["username"],
                "verbose_name": "cook",
                "verbose_name_plural": "cooks",
            },
        ),
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="dish",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]
