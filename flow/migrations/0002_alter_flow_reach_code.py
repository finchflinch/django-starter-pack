# Generated by Django 4.2.3 on 2023-07-13 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flow',
            name='reach_code',
            field=models.IntegerField(verbose_name='Reach Code'),
        ),
    ]
