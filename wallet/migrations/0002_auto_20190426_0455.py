# Generated by Django 2.2 on 2019-04-26 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='owner_addresss',
            new_name='owner_address',
        ),
    ]
