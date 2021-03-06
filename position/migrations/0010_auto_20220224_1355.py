# Generated by Django 3.0.14 on 2022-02-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0009_auto_20220223_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
