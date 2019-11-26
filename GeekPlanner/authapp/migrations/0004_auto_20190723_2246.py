# Generated by Django 2.0.13 on 2019-07-23 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20190718_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='user_avatars', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('W', 'Female')], max_length=1, verbose_name='gender'),
        ),
    ]
