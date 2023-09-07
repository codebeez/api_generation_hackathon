# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Department(models.Model):
    departmentid = models.AutoField(
        primary_key=True, db_comment="Primary key for Department records."
    )
    name = models.CharField(max_length=50, db_comment="Name of the department.")
    groupname = models.CharField(
        max_length=50, db_comment="Name of the group to which the department belongs."
    )
    modifieddate = models.DateTimeField()

    class Meta:
        db_table = "department"
        db_table_comment = "Lookup table containing the departments within the Adventure Works Cycles company."


class Employee(models.Model):
    businessentityid = models.IntegerField(
        primary_key=True,
        db_comment="Primary key for Employee records.  Foreign key to BusinessEntity.BusinessEntityID.",
    )
    nationalidnumber = models.CharField(
        max_length=15,
        db_comment="Unique national identification number such as a social security number.",
    )
    loginid = models.CharField(max_length=256, db_comment="Network login.")
    jobtitle = models.CharField(
        max_length=50, db_comment="Work title such as Buyer or Sales Representative."
    )
    birthdate = models.DateField(db_comment="Date of birth.")
    maritalstatus = models.CharField(max_length=1, db_comment="M = Married, S = Single")
    gender = models.CharField(max_length=1, db_comment="M = Male, F = Female")
    hiredate = models.DateField(db_comment="Employee hired on this date.")
    salariedflag = models.BooleanField(
        db_comment="Job classification. 0 = Hourly, not exempt from collective bargaining. 1 = Salaried, exempt from collective bargaining."
    )
    vacationhours = models.SmallIntegerField(
        db_comment="Number of available vacation hours."
    )
    sickleavehours = models.SmallIntegerField(
        db_comment="Number of available sick leave hours."
    )
    currentflag = models.BooleanField(db_comment="0 = Inactive, 1 = Active")
    rowguid = models.UUIDField()
    modifieddate = models.DateTimeField()
    organizationnode = models.CharField(
        blank=True,
        null=True,
        db_comment="Where the employee is located in corporate hierarchy.",
    )

    class Meta:
        db_table = "employee"
        db_table_comment = "Employee information such as salary, department, and title."


class Employeedepartmenthistory(models.Model):
    businessentityid = models.OneToOneField(
        Employee,
        models.DO_NOTHING,
        db_column="businessentityid",
        primary_key=True,
        db_comment="Employee identification number. Foreign key to Employee.BusinessEntityID.",
    )  # The composite primary key (businessentityid, startdate, departmentid, shiftid) found, that is not supported. The first column is selected.
    departmentid = models.ForeignKey(
        Department,
        models.DO_NOTHING,
        db_column="departmentid",
        db_comment="Department in which the employee worked including currently. Foreign key to Department.DepartmentID.",
    )
    shiftid = models.ForeignKey(
        "Shift",
        models.DO_NOTHING,
        db_column="shiftid",
        db_comment="Identifies which 8-hour shift the employee works. Foreign key to Shift.Shift.ID.",
    )
    startdate = models.DateField(
        db_comment="Date the employee started work in the department."
    )
    enddate = models.DateField(
        blank=True,
        null=True,
        db_comment="Date the employee left the department. NULL = Current department.",
    )
    modifieddate = models.DateTimeField()

    class Meta:
        db_table = "employeedepartmenthistory"
        unique_together = (
            ("businessentityid", "startdate", "departmentid", "shiftid"),
        )
        db_table_comment = "Employee department transfers."


class Employeepayhistory(models.Model):
    businessentityid = models.OneToOneField(
        Employee,
        models.DO_NOTHING,
        db_column="businessentityid",
        primary_key=True,
        db_comment="Employee identification number. Foreign key to Employee.BusinessEntityID.",
    )  # The composite primary key (businessentityid, ratechangedate) found, that is not supported. The first column is selected.
    ratechangedate = models.DateTimeField(
        db_comment="Date the change in pay is effective"
    )
    rate = models.DecimalField(
        max_digits=65535, decimal_places=65535, db_comment="Salary hourly rate."
    )
    payfrequency = models.SmallIntegerField(
        db_comment="1 = Salary received monthly, 2 = Salary received biweekly"
    )
    modifieddate = models.DateTimeField()

    class Meta:
        db_table = "employeepayhistory"
        unique_together = (("businessentityid", "ratechangedate"),)
        db_table_comment = "Employee pay history."


class Jobcandidate(models.Model):
    jobcandidateid = models.AutoField(
        primary_key=True, db_comment="Primary key for JobCandidate records."
    )
    businessentityid = models.ForeignKey(
        Employee,
        models.DO_NOTHING,
        db_column="businessentityid",
        blank=True,
        null=True,
        db_comment="Employee identification number if applicant was hired. Foreign key to Employee.BusinessEntityID.",
    )
    resume = models.TextField(
        blank=True, null=True, db_comment="RÃ©sumÃ© in XML format."
    )  # This field type is a guess.
    modifieddate = models.DateTimeField()

    class Meta:
        db_table = "jobcandidate"
        db_table_comment = "RÃ©sumÃ©s submitted to Human Resources by job applicants."


class Shift(models.Model):
    shiftid = models.AutoField(
        primary_key=True, db_comment="Primary key for Shift records."
    )
    name = models.CharField(max_length=50, db_comment="Shift description.")
    starttime = models.TimeField(db_comment="Shift start time.")
    endtime = models.TimeField(db_comment="Shift end time.")
    modifieddate = models.DateTimeField()

    class Meta:
        db_table = "shift"
        db_table_comment = "Work shift lookup table."
