# Generated by Django 5.0.4 on 2024-05-01 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hayoq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hamiyoqmi', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'hayokiyoq',
            },
        ),
        migrations.CreateModel(
            name='Ideaqomadiuje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ideabormi', models.CharField(default='yoq', max_length=255)),
            ],
            options={
                'db_table': 'idea',
            },
        ),
    ]
