# Generated by Django 4.0.7 on 2024-08-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KsBuilder', '0014_remove_vendor_quotation_paint_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_quotation',
            name='Paint_Price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='vendor_quotation',
            name='Steel_Price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='vendor_quotation',
            name='Total_Estimation',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=20),
        ),
    ]
