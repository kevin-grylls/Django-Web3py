# Generated by Django 2.2 on 2019-04-29 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0007_auto_20190429_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='origin',
            field=models.CharField(max_length=42),
        ),
    ]
