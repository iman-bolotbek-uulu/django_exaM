# Generated by Django 3.2 on 2022-12-21 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50, verbose_name='Course name')),
                ('date_started', models.DateField(verbose_name='Date started')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Course name')),
                ('month_to_learn', models.IntegerField(verbose_name='Month')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone number')),
                ('work_study_place', models.CharField(max_length=255, null=True)),
                ('has_own_notebook', models.BooleanField(default=False)),
                ('preferred_os', models.CharField(choices=[('1', 'windows'), ('2', 'mac'), ('3', 'linux')], default='1', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone number')),
                ('main_work', models.CharField(max_length=30, null=True, verbose_name='Main work')),
                ('experience', models.DateField(verbose_name='Experience')),
                ('courses', models.ManyToManyField(related_name='mentors', through='user.Course', to='user.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='course_language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.language'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.mentor'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student'),
        ),
    ]
