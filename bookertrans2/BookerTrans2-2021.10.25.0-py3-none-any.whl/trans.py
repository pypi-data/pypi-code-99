# coding: utf-8
import requests
import random
import json
from hashlib import md5
from . import config

def calc_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()

def translate(s, src='en', dst='zh'):
    salt = random.randint(32768, 65536)
    sign = calc_md5(config.appid + s + str(salt) + config.appkey)

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    param = {
        'appid': config.appid, 
        'q': s, 
        'from': src, 
        'to': dst, 
        'salt': salt, 
        'sign': sign,
    }

    j = requests.post(
        'http://api.fanyi.baidu.com/api/trans/vip/translate', 
        params=param, 
        headers=headers,
        proxies=config.proxy,
        timeout=config.timeout,
    ).json()
    if 'error_code' in j:
        raise Exception(j['error_msg'])
    return j['trans_result'][0]['dst']
