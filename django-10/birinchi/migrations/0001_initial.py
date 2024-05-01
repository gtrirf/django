# Generated by Django 5.0.4 on 2024-05-01 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ismfamilya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(blank=True, max_length=64, null=True)),
                ('familya', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'ismlar',
            },
        ),
        migrations.CreateModel(
            name='Maktab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maktabraqami', models.IntegerField(default=1)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'maktab',
            },
        ),
    ]