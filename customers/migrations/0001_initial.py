# Generated by Django 3.1.4 on 2021-01-29 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WholesaleCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=12, unique=True)),
                ('additional_phone', models.BooleanField(default=False)),
                ('phone_number2', models.CharField(blank=True, max_length=12, null=True)),
                ('additional_phone2', models.BooleanField(default=False)),
                ('phone_number3', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(blank=True, max_length=64, null=True)),
                ('additional_email', models.BooleanField(default=False)),
                ('email2', models.EmailField(blank=True, max_length=64, null=True)),
                ('additional_email2', models.BooleanField(default=False)),
                ('email3', models.EmailField(blank=True, max_length=64, null=True)),
                ('print_same', models.BooleanField(default=True)),
                ('print_name', models.CharField(max_length=100)),
                ('invoice_static', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('state', models.CharField(blank=True, choices=[('', ''), ('NC', 'NC'), ('SC', 'SC'), ('VA', 'VA'), ('KY', 'KY')], default='', max_length=2, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('notes', models.TextField(blank=True, max_length=254, null=True)),
                ('notes_popup', models.BooleanField(default=False)),
                ('is_exempt', models.BooleanField(default=False)),
                ('exemption_number', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('current_balance', models.IntegerField(blank=True, default='0', null=True)),
                ('has_credit', models.BooleanField(default=False)),
                ('credit_limit', models.IntegerField(blank=True, null=True)),
                ('credit_terms', models.CharField(blank=True, choices=[('', ''), ('Net 30', 'Net 30'), ('Net 60', 'Net 60')], default='', max_length=20, null=True)),
                ('opening_balance', models.IntegerField(blank=True, null=True)),
                ('opening_balance_date', models.DateField(blank=True, null=True)),
                ('has_attachments', models.BooleanField(default=False)),
                ('is_inactive', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
