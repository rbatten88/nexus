# Generated by Django 3.1.4 on 2021-08-16 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_loaditem_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loaditem',
            name='available',
        ),
    ]
