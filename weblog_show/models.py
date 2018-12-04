# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models



class DmDevice(models.Model):
    device = models.CharField(max_length=30, blank=True)
    num = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dm_device'

class DmKpiInfo(models.Model):
    time = models.CharField(max_length=30, blank=True)
    uv = models.IntegerField(blank=True, null=True)
    ip = models.IntegerField(blank=True, null=True)
    pv = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dm_kpi_info'

class DmSource(models.Model):
    source = models.CharField(max_length=30, blank=True)
    num = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'dm_source'

class WeblogShowTest(models.Model):
    time = models.CharField(max_length=128)
    num = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'weblog_show_test'

