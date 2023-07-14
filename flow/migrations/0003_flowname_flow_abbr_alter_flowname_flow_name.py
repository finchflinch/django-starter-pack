# Generated by Django 4.2.3 on 2023-07-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0002_alter_flow_reach_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowname',
            name='flow_abbr',
            field=models.CharField(blank=True, max_length=5, verbose_name='Flow Name Abbreviation'),
        ),
        migrations.AlterField(
            model_name='flowname',
            name='flow_name',
            field=models.CharField(max_length=200, verbose_name='name of flow'),
        ),
    ]
