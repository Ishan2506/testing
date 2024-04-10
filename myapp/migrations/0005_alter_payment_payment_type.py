# Generated by Django 5.0.1 on 2024-01-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_company_contact_alter_customer_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_type',
            field=models.BooleanField(choices=[('1', 'Cash On Delivery'), ('2', 'UPI'), ('3', 'Card')]),
        ),
    ]
