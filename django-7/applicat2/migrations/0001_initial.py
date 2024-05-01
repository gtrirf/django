# Generated by Django 5.0.4 on 2024-04-30 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.CharField(blank=True, max_length=555, null=True)),
            ],
            options={
                'db_table': 'insta',
            },
        ),
        migrations.CreateModel(
            name='Pubg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iduser', models.IntegerField(default=512)),
                ('nick', models.CharField(blank=True, max_length=255, null=True)),
                ('level', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'pubg',
            },
        ),
    ]
