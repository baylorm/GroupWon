# Generated by Django 2.2.7 on 2019-11-22 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20191110_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.Department'),
        ),
    ]
