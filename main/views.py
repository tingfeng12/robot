from django.shortcuts import render

from main import models
from django.http import HttpResponse
import base64
import urllib.parse
import hmac
from hashlib import sha1
import requests
import uuid
import time
import hmac, ssl
import logging
import json



# Create your views here.
#------------签名机制方法-----开始
def percent_encode(encodeStr):
    encodeStr = str(encodeStr)
    res = urllib.parse.quote(encodeStr)
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res


def sign(parameters,ALIYUN_ACCESS_KEY_SECRET):
    sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
    print(sortedParameters)
    canonicalizedQueryString = ''
    for (k, v) in sortedParameters:
        canonicalizedQueryString += '&' + percent_encode(k) + '=' + percent_encode(v)
    stringToSign = 'GET&%2F&' + percent_encode(canonicalizedQueryString[1:])  # 使用get请求方法
    bs = ALIYUN_ACCESS_KEY_SECRET + '&'
    bs = bytes(bs, encoding='utf8')
    stringToSign = bytes(stringToSign, encoding='utf8')
    h = hmac.new(bs, stringToSign, sha1)
    # 进行编码
    signature = base64.b64encode(h.digest()).strip()
    return signature
#------------签名机制方法-----结束


def talkingTest(request):
	tesrRobotId = "chatbot-cn-4591d9l7a0002t"

	platformAccountUserName = "1624471394743441"
	platformAccountLoginName = "znz980"
	platformAccountMobile = ""
	platformAccountEmail = ""
	platform_type = "aliyun_yunme"
	ID = "LTAI4FcuXo5qxQo3Ce5Chp9p"
	S = "MQdnYqV5TJba7ORMMc7qXHwPEoQyQg"

	print(models.CPlatformAccount)
	res = models.CPlatformAccount.objects.values('id')
	print(res)

	D = {
		'Format': 'JSON',  # 返回值的类型
		'Version': '2017-10-11',  # API 版本号
		'SignatureMethod': 'HMAC-SHA1',  # 签名方式
		'SignatureVersion': 1.0,  # 签名算法版本
		'AccessKeyId':ID,
		'Action' : "Chat",  # 必要参数
		'InstanceId' : "chatbot-cn-4591d9l7a0002t",  # 你阿里云的机器人实例id
		"SessionId":"54e6a931794143a18654f9f24b13f74f"
	}

	D['SignatureNonce'] = str(uuid.uuid1())  # 唯一随机数，用于防止网络重放攻击。
	D['Timestamp'] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())  #
	D['Utterance'] = '你好'
	q = request.GET['q']
	if(q):
		D['Utterance'] = q	# 问题


	D['Signature'] = sign(D,S)  # 签名结果串
	sortedParameters = sorted(D.items(), key=lambda D: D[0])
	# sorted(d.items(), key=lambda x: x[1]) 中 d.items() 为待排序的对象；key=lambda x: x[1] 为对前面的对象中的第二维数据（即value）的值进行排序。 key=lambda 变量：变量[维数] 。维数可以按照自己的需要进行设置。
	# print(D["Signature"])
	# print(sortedParameters)

	url = 'https://chatbot.cn-shanghai.aliyuncs.com/?' + urllib.parse.urlencode(sortedParameters)
	print(url)
	r = requests.get(url)
	print('---------------------------------')
	print(r.text)
	# print(type(r.text))

	# print(json.loads(r.text)['Messages'][0]['Text']['Content'])


	return HttpResponse(r.text)



def selecting(event):
	logger = logging.getLogger()
	logger.info(event)
	slots = event.GET['tim']
	print(slots)
	# slots = eventObj["tim"]
	logger.info(slots)
	# orderId = slots[u"请假意图.天数"]
	if slots >=5:
		eventObj["global"]["obje"] = "长假"
	else:
		eventObj["global"]["obje"] = "短假"
	print(eventObj["global"]["obje"])
	print('--------------------------------------------------------------------')
	print(eventObj)
	return eventObj

