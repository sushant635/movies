# Generated by Django 3.2 on 2021-05-06 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20210506_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='uuid',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
