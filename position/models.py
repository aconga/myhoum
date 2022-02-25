from django.db import models
from datetime import datetime
from django.utils import timezone
import haversine as hs
from django.contrib.auth.models import User
# signals
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

class Property(models.Model):
    address = models.CharField(max_length=100, blank=True, null=True)
    houm = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='propertys')
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    visited = models.BooleanField(default=False)
    register = models.DateField(default=timezone.now)
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('-start_date',)
    def __str__(self):
        return self.address


@receiver(post_save, sender=Property)
def create_finish_date(sender, instance, **kwargs):
    if instance.finish_date:
        a_timedelta = instance.finish_date - instance.start_date
        total_time_sec = a_timedelta.total_seconds()
        property_info, created = PropertyInfo.objects.get_or_create(property=instance)
        property_info.total_time_sec = total_time_sec
        property_info.save()


class PropertyInfo(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    property = models.OneToOneField(Property,
                              on_delete=models.CASCADE,
                              related_name='property_details')
    total_time_sec = models.IntegerField(blank=True, null=True)
    speed = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return "PropertyInfo {}".format(self.description)
