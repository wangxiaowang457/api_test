# -*- encoding=utf8 -*-
__author__ = "wangbingqian"

import os
from common import comm_steps,readConf,httprequest
import json
from common.db import db
import unittest

'''
执行tag
case_tag: api,001,public-contentdistribute-portalweb,sit
'''

"""
数据库里读取数据
"""
data = db.mySql().mselectSql("select_manual_tags",[28,10],"db")
#print("data11: ",data)

#请求接口url
host = comm_steps.get_api_url()
url = "/distribute-service/distribute/manualLabel/queryManualTagsByFuzzy"
url = host + url
print("接口请求url: ",url)

"""
param: 业务参数
headers: header参数
"""

headers = comm_steps.get_header_data()
print("请求cookie: ",headers)
param = {
    'name':'呵呵'
}

exId = data[0][0]
exTag = data[0][1]
print("exId,exTag: ",exId,exTag)

result = httprequest.sendRequest().send(url,'GET',param,headers)



