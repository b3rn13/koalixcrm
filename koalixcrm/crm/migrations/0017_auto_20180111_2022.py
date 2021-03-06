# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-11 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0016_auto_20180111_2011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailaddressforsalesdocument',
            options={'verbose_name': 'Email Address For Contract', 'verbose_name_plural': 'Email Address For Contracts'},
        ),
        migrations.AlterModelOptions(
            name='phoneaddressforsalesdocument',
            options={'verbose_name': 'Phone Address For Sales Contract', 'verbose_name_plural': 'Phone Address For Contracts'},
        ),
        migrations.AlterModelOptions(
            name='postaladdressforsalesdocument',
            options={'verbose_name': 'Postal Address For Contract', 'verbose_name_plural': 'Postal Address For Contracts'},
        ),
        migrations.AlterModelOptions(
            name='salesdocument',
            options={'verbose_name': 'Sales Document', 'verbose_name_plural': 'Sales Documents'},
        ),
        migrations.AlterModelOptions(
            name='salesdocumentposition',
            options={'verbose_name': 'Position in Sales Document', 'verbose_name_plural': 'Positions Sales Document'},
        ),
        migrations.AlterField(
            model_name='position',
            name='last_calculated_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=17, null=True, verbose_name='Last Calculated Price'),
        ),
        migrations.AlterField(
            model_name='position',
            name='last_calculated_tax',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=17, null=True, verbose_name='Last Calculated Tax'),
        ),
    ]
