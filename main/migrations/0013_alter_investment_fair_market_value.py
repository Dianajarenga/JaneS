# Generated by Django 3.2.8 on 2021-12-04 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20211202_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='fair_market_value',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
