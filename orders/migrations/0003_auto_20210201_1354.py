# Generated by Django 3.1.4 on 2021-02-01 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210201_1341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='number',
            new_name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
    ]