# -*- coding:utf-8 -*-
"""
Author:duan
Date:2019/4/15 12:51
"""
import json
import requests
from json import JSONDecodeError

FILENAME = 'city_code.txt'


def read_code(filename=FILENAME):
    with open(filename, 'r') as f:
        city_code = json.load(f)
    return city_code


def query_code(city_codes, city_name):
    '''
    city_codes:城市代码字典
    city:字符串
    '''
    try:
        code = city_codes[city_name]
    except KeyError:
        raise
    return code


def query_weather(code):
    html = f'http://wthrcdn.etouch.cn/weather_mini?citykey={code}'

    try:
        info = requests.get(html)
        info.encoding = 'utf-8'
    except requests.ConnectionError:
        raise

    try:
        info_json = info.json()
    except JSONDecodeError:
        return '无法查询'
    # 天气情况
    data = info_json['data']
    city = data['city']
    today = data['forecast'][0]
    date = today['date']
    now = data['wendu']
    temperature = today['high'] + today['low']
    fengxiang = today['fengxiang']
    type = today['type']
    tips = data['ganmao']

    weather = {
        'city': city,
        'date': date,
        'now': now,
        'temperature': temperature,
        'fengxiang': fengxiang,
        'type': type,
        'tips': tips
    }
    return weather
