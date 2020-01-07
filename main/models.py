from django.db import models
"""
数据库要求：
	数据库名：robot
	字符集：utf8
	排序规则：utf8_bin

数据库链接规则(账号密码等)，请在/robot/settings.py中DATABASES变量里配置

models配置指南：https://www.jianshu.com/p/bf3a8fc93214

生成、创建及更新数据表结构的命令：
	python manage.py makemigrations
	python manage.py migrate
"""

# 第三方机器人平台账户表
class CPlatformAccount(models.Model):
	id = models.AutoField(primary_key=True)

	user_id = models.CharField(max_length=32)
	login_name = models.CharField(max_length=18, blank=True, null=True)
	mobile = models.CharField(max_length=18, blank=True, null=True)
	email = models.CharField(max_length=18, blank=True, null=True)
	platform_type = models.CharField(max_length=64, blank=True, null=True)
	access_key_id = models.CharField(max_length=64, blank=True, null=True)
	access_key_secret = models.CharField(max_length=64, blank=True, null=True)
	remark = models.TextField(blank=True, null=True)

	status = models.SmallIntegerField(default = 1)
	created_at = models.DateTimeField(blank=True, null=True)
	created_by = models.CharField(max_length=64, blank=True, null=True)
	updated_at = models.DateTimeField(blank=True, null=True)
	updated_by = models.CharField(max_length=64, blank=True, null=True)

	class Meta:
		# managed = False
		db_table = 'c_platform_account'

# 第三方机器人实例表
class CPlatformInstence (models.Model):
	id = models.AutoField(primary_key=True,max_length=255)
	platform_account_id = models.IntegerField()
	instence_id = models.CharField(max_length=64, blank=True, null=True)
	remark = models.TextField(blank=True, null=True)

	status = models.SmallIntegerField(default = 1)
	created_at = models.DateTimeField(blank=True, null=True)
	created_by = models.CharField(max_length=64, blank=True, null=True)
	updated_at = models.DateTimeField(blank=True, null=True)
	updated_by = models.CharField(max_length=64, blank=True, null=True)
	
	class Meta:
		managed = True
		db_table = 'c_platform_instence'