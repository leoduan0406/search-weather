# -*- coding:utf-8 -*-
"""
Author:duan
Date:2019/4/15 12:51
"""
import json
import re

import pandas as pd

file = pd.read_csv('city_code.csv')
file = file.loc[:, ['City_ID', 'City_CN']]


def convert(x):
    pat = re.compile('(\d+)')
    return pat.search(x).group()


file['City_ID_map'] = file['City_ID'].map(convert)


def city2id(file):
    code_dict = {}
    key = 'City_CN'
    value = 'City_ID_map'
    for k, v in zip(file[key], file[value]):
        code_dict[k] = v
    return code_dict


code_dict = city2id(file)
filename = 'city_code2.txt'
with open(filename, 'wb') as f:
    json.dump(code_dict, f)
