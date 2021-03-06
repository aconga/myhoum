# Generated by Django 3.0.14 on 2022-02-23 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.SlugField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('register', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('finish_date', models.DateTimeField(auto_now=True)),
                ('houm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propertys', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-register',),
            },
        ),
    ]
