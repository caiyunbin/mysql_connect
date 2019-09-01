# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 23:21:27 2019

@author: caiyu
"""

import pymysql

db=pymysql.connect(host='localhost',user='root',password='caiyunbin3344',port=3306)
cursor=db.cursor()
cursor.execute('SELECT VERSION()')
data=cursor.fetchone()
print('database version:',data)
cursor.execute('CREATE DATABASE spiders')
db.close










