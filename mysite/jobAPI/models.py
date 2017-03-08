# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Job(models.Model):
    positionname = models.TextField(db_column='positionName', blank=True, null=True)  # Field name made lowercase.
    salary = models.CharField(max_length=10, blank=True, null=True)
    workyear = models.CharField(db_column='workYear', max_length=10, blank=True, null=True)  # Field name made lowercase.
    education = models.CharField(max_length=10, blank=True, null=True)
    industryfield = models.CharField(db_column='industryField', max_length=40, blank=True, null=True)  # Field name made lowercase.
    companyshortname = models.CharField(db_column='companyShortName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    companyfullname = models.TextField(db_column='companyFullName', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(max_length=20, blank=True, null=True)
    district = models.CharField(max_length=20, blank=True, null=True)
    businesszones = models.TextField(db_column='businessZones', blank=True, null=True)  # Field name made lowercase.
    financestage = models.TextField(db_column='financeStage', blank=True, null=True)  # Field name made lowercase.
    companylabellist = models.TextField(db_column='companyLabelList', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'job'