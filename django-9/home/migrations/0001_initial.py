# Generated by Django 5.0.4 on 2024-05-01 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrueorFalse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atvet', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'atvet',
            },
        ),
        migrations.CreateModel(
            name='YesorNO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otvet', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'otvet',
            },
        ),
    ]
