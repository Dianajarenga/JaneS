# Generated by Django 3.2.8 on 2021-12-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_investment_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=150)),
                ('total_commited', models.IntegerField()),
                ('net_investment', models.IntegerField()),
                ('total_bhi_shares_remaining', models.IntegerField()),
                ('latest_share_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fair_market_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_coc_returns', models.DecimalField(decimal_places=2, max_digits=5)),
                ('year', models.IntegerField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='investment',
            name='company',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='fair_market_value',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='latest_share_price',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='net_investment',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='total_bhi_shares_remaining',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='total_coc_returns',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='total_commited',
        ),
    ]