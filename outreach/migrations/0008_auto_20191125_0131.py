# Generated by Django 2.2.7 on 2019-11-25 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outreach', '0007_auto_20191124_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='num_volunteers',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of Volunteers'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='type',
            field=models.CharField(choices=[('Community Organization', 'Community Organization'), ('Club', 'Club'), ('Course', 'Course')], max_length=150),
        ),
    ]
