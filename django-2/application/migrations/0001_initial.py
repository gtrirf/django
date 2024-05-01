# Generated by Django 5.0.4 on 2024-04-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('where', models.CharField(blank=True, max_length=255, null=True)),
                ('jobname', models.CharField(blank=True, max_length=255, null=True)),
                ('sallary', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=255, null=True)),
                ('lastname', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'names',
            },
        ),
    ]
