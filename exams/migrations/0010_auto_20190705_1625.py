# Generated by Django 2.2.3 on 2019-07-05 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_auto_20190630_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finishedexams',
            name='full_mark',
        ),
        migrations.AddField(
            model_name='exam',
            name='full_mark',
            field=models.IntegerField(default=100),
        ),
    ]
