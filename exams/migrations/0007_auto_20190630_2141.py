# Generated by Django 2.2 on 2019-06-30 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_auto_20190630_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='blank_avatar.png', upload_to='personal/%y/%m/'),
        ),
    ]
