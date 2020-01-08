# Generated by Django 3.0.2 on 2020-01-08 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191118_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('courseid', models.CharField(blank=True, db_column='courseId', max_length=20, null=True)),
                ('matric', models.CharField(blank=True, max_length=10, null=True)),
                ('feedback', models.CharField(blank=True, max_length=100, null=True)),
                ('duedate', models.DateField(blank=True, db_column='dueDate', null=True)),
                ('status', models.BooleanField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'assignment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseid', models.BigAutoField(db_column='courseId', primary_key=True, serialize=False)),
                ('coursecode', models.CharField(blank=True, db_column='courseCode', max_length=10, null=True)),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('year', models.CharField(blank=True, max_length=10, null=True)),
                ('group', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Courseperformance',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('courseid', models.IntegerField(blank=True, null=True)),
                ('matric', models.CharField(blank=True, max_length=10, null=True)),
                ('attendance', models.FloatField(blank=True, null=True)),
                ('cps4w7', models.FloatField(blank=True, db_column='cps4W7', null=True)),
                ('cps7w7', models.FloatField(blank=True, db_column='cps7W7', null=True)),
                ('cps4w14', models.FloatField(blank=True, db_column='cps4W14', null=True)),
                ('cps7w14', models.FloatField(blank=True, db_column='cps7W14', null=True)),
                ('amali', models.FloatField(blank=True, null=True)),
                ('quiz', models.FloatField(blank=True, null=True)),
                ('cps4final', models.FloatField(blank=True, db_column='cps4Final', null=True)),
                ('cps7final', models.FloatField(blank=True, db_column='cps7Final', null=True)),
                ('cps8final', models.FloatField(blank=True, db_column='cps8Final', null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('status', models.BooleanField(blank=True, null=True)),
                ('cousecode', models.CharField(blank=True, db_column='couseCode', max_length=10, null=True)),
                ('week7', models.FloatField(blank=True, null=True)),
                ('week14', models.FloatField(blank=True, null=True)),
                ('totalt1t2', models.FloatField(blank=True, db_column='totalT1T2', null=True)),
                ('totalcarrymark', models.FloatField(blank=True, db_column='totalCarryMark', null=True)),
                ('predictedmarks', models.FloatField(blank=True, db_column='predictedMarks', null=True)),
            ],
            options={
                'db_table': 'coursePerformance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('programid', models.CharField(db_column='programId', max_length=10, primary_key=True, serialize=False)),
                ('programname', models.CharField(blank=True, db_column='programName', max_length=10, null=True)),
                ('intake', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'program',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Data',
        ),
        migrations.DeleteModel(
            name='Performance',
        ),
        migrations.AlterModelOptions(
            name='account',
            options={'managed': False},
        ),
    ]