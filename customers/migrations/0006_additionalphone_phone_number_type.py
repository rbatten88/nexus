# Generated by Django 3.1.4 on 2021-01-09 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_wholesalecustomer_phone_number_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalphone',
            name='phone_number_type',
            field=models.CharField(choices=[('m', 'Mobile'), ('o', 'Office')], default='o', max_length=1),
        ),
    ]