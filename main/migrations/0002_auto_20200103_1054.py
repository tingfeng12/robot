# Generated by Django 3.0 on 2020-01-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPlatformInstence',
            fields=[
                ('id', models.AutoField(max_length=255, primary_key=True, serialize=False)),
                ('platform_account_id', models.IntegerField()),
                ('instence_id', models.CharField(blank=True, max_length=64, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=64, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'c_platform_instence',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='cplatformaccount',
            options={'managed': False},
        ),
    ]
