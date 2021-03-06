# Generated by Django 3.0 on 2020-01-03 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPlatformAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=32)),
                ('login_name', models.CharField(blank=True, max_length=18, null=True)),
                ('mobile', models.CharField(blank=True, max_length=18, null=True)),
                ('email', models.CharField(blank=True, max_length=18, null=True)),
                ('platform_type', models.CharField(blank=True, max_length=64, null=True)),
                ('access_key_id', models.CharField(blank=True, max_length=64, null=True)),
                ('access_key_secret', models.CharField(blank=True, max_length=64, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('status', models.SmallIntegerField(default=1)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=64, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'c_platform_account',
                'managed': True,
            },
        ),
    ]
