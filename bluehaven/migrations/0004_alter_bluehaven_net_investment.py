# Generated by Django 3.2.8 on 2021-12-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluehaven', '0003_alter_bluehaven_net_investment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bluehaven',
            name='net_investment',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]