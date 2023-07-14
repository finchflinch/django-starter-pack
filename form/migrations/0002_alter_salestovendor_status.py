# Generated by Django 4.2.3 on 2023-07-13 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salestovendor',
            name='status',
            field=models.CharField(choices=[('APPROVED', 'Approved'), ('IN_PROCESS', 'In Process'), ('REJECTED', 'Rejected'), ('ON_HOLD', 'On Hold')], default='IN_PROCESS', max_length=15, verbose_name='Form Status'),
        ),
    ]
