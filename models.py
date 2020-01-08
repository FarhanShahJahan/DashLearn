# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsAccount(models.Model):
    password = models.CharField(max_length=140)
    program = models.CharField(max_length=120)
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField()
    is_admin = models.BooleanField()
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    matric = models.CharField(unique=True, max_length=10)
    cgpa = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    cgpapercent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_account'


class Assignment(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.CharField(db_column='courseId', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    matric = models.CharField(max_length=-1, blank=True, null=True)
    feedback = models.CharField(max_length=-1, blank=True, null=True)
    duedate = models.DateField(db_column='dueDate', blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assignment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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


class Course(models.Model):
    courseid = models.BigAutoField(db_column='courseId', primary_key=True)  # Field name made lowercase.
    coursecode = models.CharField(db_column='courseCode', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    semester = models.IntegerField(blank=True, null=True)
    year = models.CharField(max_length=-1, blank=True, null=True)
    group = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Courseperformance(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.IntegerField(blank=True, null=True)
    matric = models.CharField(max_length=-1, blank=True, null=True)
    attendance = models.FloatField(blank=True, null=True)
    cps4w7 = models.FloatField(db_column='cps4W7', blank=True, null=True)  # Field name made lowercase.
    cps7w7 = models.FloatField(db_column='cps7W7', blank=True, null=True)  # Field name made lowercase.
    cps4w14 = models.FloatField(db_column='cps4W14', blank=True, null=True)  # Field name made lowercase.
    cps7w14 = models.FloatField(db_column='cps7W14', blank=True, null=True)  # Field name made lowercase.
    amali = models.FloatField(blank=True, null=True)
    quiz = models.FloatField(blank=True, null=True)
    cps4final = models.FloatField(db_column='cps4Final', blank=True, null=True)  # Field name made lowercase.
    cps7final = models.FloatField(db_column='cps7Final', blank=True, null=True)  # Field name made lowercase.
    cps8final = models.FloatField(db_column='cps8Final', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    cousecode = models.CharField(db_column='couseCode', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    week7 = models.FloatField(blank=True, null=True)
    week14 = models.FloatField(blank=True, null=True)
    totalt1t2 = models.FloatField(db_column='totalT1T2', blank=True, null=True)  # Field name made lowercase.
    totalcarrymark = models.FloatField(db_column='totalCarryMark', blank=True, null=True)  # Field name made lowercase.
    predictedmarks = models.FloatField(db_column='predictedMarks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coursePerformance'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsAccount, models.DO_NOTHING)

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


class Marks(models.Model):
    matric = models.CharField(primary_key=True, max_length=-1)
    su1 = models.IntegerField(blank=True, null=True)
    smid = models.IntegerField(blank=True, null=True)
    sfin = models.IntegerField(blank=True, null=True)
    att = models.FloatField(blank=True, null=True)
    mu1 = models.IntegerField(blank=True, null=True)
    mmid = models.IntegerField(blank=True, null=True)
    mfin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marks'


class Program(models.Model):
    programid = models.CharField(db_column='programId', primary_key=True, max_length=-1)  # Field name made lowercase.
    programname = models.CharField(db_column='programName', max_length=-1, blank=True, null=True)  # Field name made lowercase.
    intake = models.IntegerField(blank=True, null=True)
    faculty = models.CharField(db_column='Faculty', max_length=-1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'program'
