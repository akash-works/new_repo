# Generated by Django 4.0.6 on 2022-07-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_hvs_student_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hvs',
            name='student_age',
        ),
        migrations.AddField(
            model_name='hvs',
            name='contents',
            field=models.TextField(blank=True),
        ),
    ]
