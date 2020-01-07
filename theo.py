import base64
import urllib.parse
import hmac
from hashlib import sha1
import requests
import uuid
import time
import hmac, ssl
import json


ALIYUN_ACCESS_KEY_ID = "LTAI4FgC6jCHjDPM7VuGgDh9"
ALIYUN_ACCESS_KEY_SECRET = "lLk2lmLLD5FGFxErkGzaQv2A92oo9x"
# 解决 访问ssl网站证书的问题
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
D = {
    'Format': 'JSON',       #返回值的类型
    'Version': '2017-10-11',        #API 版本号
    'SignatureMethod': 'HMAC-SHA1'      #签名方式
}

timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
D['SignatureNonce'] = str(uuid.uuid1())         #唯一随机数，用于防止网络重放攻击。
D['SignatureVersion'] = 1.0         #签名算法版本
D['AccessKeyId'] = ALIYUN_ACCESS_KEY_ID
D['Timestamp'] = timestamp      #请求的时间戳


def percent_encode(encodeStr):      #签名机制方法
    encodeStr = str(encodeStr)
    res = urllib.parse.quote(encodeStr)
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res


def sign(parameters):           #签名机制方法
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


D['Action'] = "Chat"    #必要参数
D['InstanceId'] = "chatbot-cn-aqir6uMeaa"  # 你阿里云的机器人实例id
D['Utterance'] = "你是谁"   #问题
D['Signature'] = sign(D)  #签名结果串
sortedParameters = sorted(D.items(), key=lambda D: D[0])
# print(D["Signature"])
# print(sortedParameters)

url = 'https://chatbot.cn-shanghai.aliyuncs.com/?' + urllib.parse.urlencode(sortedParameters)
print(url)
r = requests.get(url)
print('---------------------------------')
print(r.text)
# print(json.loads(r.text))
print(json.loads(r.text)['Messages'][0]['Text']['Content'])
# print(type(json.loads(r.text)['Messages'][0]['Text']['Content']))