# Generated by Django 5.1.2 on 2024-10-21 00:44

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-date_join']},
        ),
        migrations.RemoveField(
            model_name='student',
            name='cohort',
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='student',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='student',
            name='program',
        ),
        migrations.RemoveField(
            model_name='student',
            name='rating',
        ),
        migrations.AddField(
            model_name='student',
            name='date_join',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default=1, max_length=200, verbose_name='last name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_type',
            field=models.CharField(choices=[('leader', 'cohort leader'), ('deputy', 'vice leader'), ('secretary', 'secretary'), ('President', 'President'), ('member', 'member')], default='member', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default=111111, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='CohortGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_join', models.DateTimeField(auto_now_add=True)),
                ('students', models.ManyToManyField(to='students.student')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.CharField(max_length=500)),
                ('grade', models.IntegerField(default=0.0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=300)),
                ('rating', models.FloatField(default=0.0)),
                ('profile_picture', models.ImageField(upload_to='student_profile')),
                ('date_join', models.DateTimeField(auto_now_add=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]
