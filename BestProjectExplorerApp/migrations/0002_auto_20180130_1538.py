# Generated by Django 2.0 on 2018-01-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BestProjectExplorerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='grant_type',
            field=models.CharField(choices=[('SSG', 'Swift Small Grant'), ('SG', 'Small Grant'), ('MG', 'Medium Grant')], max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='main_subject',
            field=models.CharField(choices=[('CR', 'Coral Restoration'), ('IAS', 'IAS Control'), ('HR', 'Habitat Restoration'), ('SC', 'Species Conservation')], max_length=255),
        ),
    ]