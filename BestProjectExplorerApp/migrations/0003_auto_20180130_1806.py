# Generated by Django 2.0 on 2018-01-30 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BestProjectExplorerApp', '0002_auto_20180130_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='monthly_report',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='unit',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='target',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
