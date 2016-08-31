# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    address_id = models.BigIntegerField(db_column='Address_id', primary_key=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=50)  # Field name made lowercase.
    vdc_municipality = models.CharField(db_column='VDC_Municipality', max_length=50)  # Field name made lowercase.
    wardno = models.CharField(db_column='WardNo', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Address'


class Area(models.Model):
    area_id = models.BigIntegerField(db_column='Area_id', primary_key=True)  # Field name made lowercase.
    area_no = models.IntegerField(db_column='Area_no')  # Field name made lowercase.
    area_district = models.CharField(db_column='Area_district', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Area'


class Candidate(models.Model):
    can_id = models.BigIntegerField(db_column='Can_id', primary_key=True)  # Field name made lowercase.
    can_fullname = models.CharField(db_column='Can_fullName', max_length=50)  # Field name made lowercase.
    can_gender = models.CharField(db_column='Can_gender', max_length=10)  # Field name made lowercase.
    can_dob = models.DateField(db_column='Can_dob')  # Field name made lowercase.
    can_photo = models.TextField(db_column='Can_photo', blank=True, null=True)  # Field name made lowercase.
    can_fathername = models.CharField(db_column='Can_fatherName', max_length=50)  # Field name made lowercase.
    can_address_id = models.BigIntegerField(db_column='Can_Address_id')  # Field name made lowercase.
    can_area_id = models.BigIntegerField(db_column='Can_Area_id')  # Field name made lowercase.
    can_party_id = models.BigIntegerField(db_column='Can_Party_id', blank=True, null=True)  # Field name made lowercase.
    can_mover_id = models.BigIntegerField(db_column='Can_Mover_id', blank=True, null=True)  # Field name made lowercase.
    can_supp_id = models.BigIntegerField(db_column='Can_Supp_id', blank=True, null=True)  # Field name made lowercase.
    can_voter_id = models.IntegerField(db_column='Can_Voter_id', blank=True, null=True)  # Field name made lowercase.
    can_date = models.DateField(db_column='Can_date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Candidate'


class Citizenship(models.Model):
    citizenship_id = models.CharField(db_column='Citizenship_id', primary_key=True, max_length=20)  # Field name made lowercase.
    citizenshiptype = models.CharField(db_column='CitizenshipType', max_length=20)  # Field name made lowercase.
    birthdistrict = models.CharField(db_column='BirthDistrict', max_length=20)  # Field name made lowercase.
    issuedate = models.DateField(db_column='IssueDate')  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    issuedaddress_id = models.BigIntegerField(db_column='IssuedAddress_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Citizenship'


class Disability(models.Model):
    disability_id = models.CharField(db_column='Disability_id', primary_key=True, max_length=5)  # Field name made lowercase.
    disabilitydescription = models.CharField(db_column='DisabilityDescription', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disability'


class Mover(models.Model):
    mover_id = models.BigIntegerField(db_column='Mover_id', primary_key=True)  # Field name made lowercase.
    mover_fullname = models.CharField(db_column='Mover_fullName', max_length=50)  # Field name made lowercase.
    mover_dob = models.DateField(db_column='Mover_dob')  # Field name made lowercase.
    mover_gender = models.CharField(db_column='Mover_gender', max_length=10)  # Field name made lowercase.
    mover_fathername = models.CharField(db_column='Mover_fatherName', max_length=50)  # Field name made lowercase.
    mover_voter_id = models.IntegerField(db_column='Mover_Voter_id', blank=True, null=True)  # Field name made lowercase.
    mover_address_id = models.BigIntegerField(db_column='Mover_Address_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mover'


class Party(models.Model):
    party_id = models.BigIntegerField(db_column='Party_id', primary_key=True)  # Field name made lowercase.
    party_name = models.CharField(db_column='Party_name', max_length=50)  # Field name made lowercase.
    party_stamp = models.TextField(db_column='Party_Stamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Party'


class Pledge(models.Model):
    pl_voucherno = models.IntegerField(db_column='Pl_voucherNo', primary_key=True)  # Field name made lowercase.
    pl_bankname = models.CharField(db_column='Pl_bankName', max_length=50)  # Field name made lowercase.
    pl_can_id = models.BigIntegerField(db_column='Pl_Can_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pledge'


class Supporter(models.Model):
    supp_id = models.BigIntegerField(db_column='Supp_id', primary_key=True)  # Field name made lowercase.
    supp_fullname = models.CharField(db_column='Supp_fullName', max_length=50)  # Field name made lowercase.
    supp_dob = models.DateField(db_column='Supp_dob')  # Field name made lowercase.
    supp_gender = models.CharField(db_column='Supp_gender', max_length=10)  # Field name made lowercase.
    supp_fathername = models.CharField(db_column='Supp_fatherName', max_length=50)  # Field name made lowercase.
    supp_photo = models.TextField(db_column='Supp_photo')  # Field name made lowercase.
    supp_voter_id = models.IntegerField(db_column='Supp_Voter_id', blank=True, null=True)  # Field name made lowercase.
    supp_address_id = models.BigIntegerField(db_column='Supp_Address_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Supporter'


class VoterInfo(models.Model):
    voter_id = models.IntegerField(db_column='Voter_id', primary_key=True)  # Field name made lowercase.
    citizenship = models.ForeignKey(Citizenship, models.DO_NOTHING, db_column='Citizenship_id')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1)  # Field name made lowercase.
    spousename = models.CharField(db_column='SpouseName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=50)  # Field name made lowercase.
    grandfathername = models.CharField(db_column='GrandFatherName', max_length=50)  # Field name made lowercase.
    mothertongue = models.CharField(db_column='MotherTongue', max_length=50)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    literacystatus = models.CharField(db_column='LiteracyStatus', max_length=1)  # Field name made lowercase.
    qualification = models.CharField(db_column='Qualification', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address_id = models.IntegerField(db_column='Address_id')  # Field name made lowercase.
    disability = models.ForeignKey(Disability, models.DO_NOTHING, db_column='Disability_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Voter_info'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CandidateInfo(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'candidate_info'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
