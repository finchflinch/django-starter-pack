# Generated by Django 4.2.3 on 2023-07-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.CharField(default='1100', max_length=5, verbose_name='Company code'),
        ),
    ]
