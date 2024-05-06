# Generated by Django 5.0.4 on 2024-05-01 13:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_staffs'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Група студентів',
                'verbose_name_plural': 'Групи студентів',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Дисципліна',
                'verbose_name_plural': 'Дисципліни',
            },
        ),
        migrations.AlterModelOptions(
            name='staffs',
            options={'verbose_name': 'Інф. користувача', 'verbose_name_plural': 'Інф. користувачів'},
        ),
        migrations.CreateModel(
            name='StudentGroupLinks',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.studentgroups')),
            ],
        ),
        migrations.CreateModel(
            name='TeachingAssignments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.studentgroups')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.subjects')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
