# Generated by Django 3.0.14 on 2022-02-24 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('position', '0011_auto_20220224_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='houm',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='propertys', to=settings.AUTH_USER_MODEL),
        ),
    ]
