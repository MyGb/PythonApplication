from django.db import models

# Create your models here.
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