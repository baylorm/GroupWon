# Generated by Django 2.2.7 on 2019-11-10 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('notes', models.TextField()),
            ],
        ),
    ]
