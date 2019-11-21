# Generated by Django 2.2.6 on 2019-11-17 15:58

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.IntegerField(blank=True, null=True)),
                ('test1', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('matric', models.IntegerField(db_column='Matric', primary_key=True, serialize=False)),
                ('su1', models.IntegerField(blank=True, db_column='SU1', null=True)),
                ('smid', models.IntegerField(blank=True, db_column='Smid', null=True)),
                ('sfin', models.IntegerField(blank=True, db_column='Sfin', null=True)),
                ('att', models.FloatField(blank=True, db_column='Att', null=True)),
                ('mu1', models.IntegerField(blank=True, db_column='MU1', null=True)),
                ('mmid', models.IntegerField(blank=True, db_column='Mmid', null=True)),
                ('mfin', models.IntegerField(blank=True, db_column='Mfin', null=True)),
            ],
            options={
                'db_table': 'marks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matric', models.IntegerField(blank=True, db_column='Matric', null=True)),
                ('su1', models.IntegerField(blank=True, db_column='SU1', null=True)),
                ('smid', models.IntegerField(blank=True, db_column='Smid', null=True)),
                ('sfin', models.IntegerField(blank=True, db_column='Sfin', null=True)),
                ('att', models.FloatField(blank=True, db_column='Att', null=True)),
                ('mu1', models.IntegerField(blank=True, db_column='MU1', null=True)),
                ('mmid', models.IntegerField(blank=True, db_column='Mmid', null=True)),
                ('mfin', models.IntegerField(blank=True, db_column='Mfin', null=True)),
            ],
            options={
                'db_table': 'performance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True, verbose_name='username')),
                ('password', models.CharField(max_length=140)),
                ('program', models.CharField(max_length=120)),
                ('faculty', models.CharField(max_length=130)),
                ('department', models.CharField(max_length=20)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]