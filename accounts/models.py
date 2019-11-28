from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self,matric,password,program):
        if not matric:
            raise ValueError("Enter Matric ID")
        if not password:
            raise ValueError("Enter Password")
        if not program:
            raise ValueError("Enter program")
        user = self.model(
            matric=matric,
            program=program,
            password=password

        )
        user.save(using=self._db)
        return user

    def create_superuser(self,matric,program,password):
        user = self.create_user(
            matric=matric,
            program=program,
            password=password
        )
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
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
    name = models.CharField(max_length=20, blank=True, null=True)

    
    class Meta:
        managed = False
        db_table = 'accounts_account'

    USERNAME_FIELD = 'matric'
    REQUIRED_FIELD = ['program','password']

    objects = MyAccountManager() 

    def __str__(self):
        return self.matric

    def has_perm(self,prem,obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


#--------------------------------------------------------------------------------

class Marks(models.Model):
    matric = models.CharField(primary_key=True, max_length=10)
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

class Courseperformance(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.IntegerField(blank=True, null=True)
    matric = models.CharField(max_length=10, blank=True, null=True)
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
    cousecode = models.CharField(db_column='couseCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    week7 = models.FloatField(blank=True, null=True)
    week14 = models.FloatField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'coursePerformance'

class Program(models.Model):
    programid = models.CharField(db_column='programId', primary_key=True, max_length=10)  # Field name made lowercase.
    programname = models.CharField(db_column='programName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    intake = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'program'

class Course(models.Model):
    courseid = models.BigAutoField(db_column='courseId', primary_key=True)  # Field name made lowercase.
    coursecode = models.CharField(db_column='courseCode', max_length=10, blank=True, null=True)  # Field name made lowercase.
    semester = models.IntegerField(blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    group = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'

class Assignment(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.CharField(db_column='courseId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    matric = models.CharField(max_length=10, blank=True, null=True)
    feedback = models.CharField(max_length=100, blank=True, null=True)
    duedate = models.DateField(db_column='dueDate', blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assignment'
