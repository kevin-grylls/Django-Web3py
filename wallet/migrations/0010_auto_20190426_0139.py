# Generated by Django 2.2 on 2019-04-26 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0009_auto_20190426_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='owner',
            field=models.CharField(max_length=42),
        ),
    ]