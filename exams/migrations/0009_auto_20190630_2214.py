# Generated by Django 2.2 on 2019-06-30 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0008_auto_20190630_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='birth_dat',
            new_name='birth_date',
        ),
    ]