# Generated by Django 3.2.8 on 2021-11-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_investment_initial_investment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='fund_ownership',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
