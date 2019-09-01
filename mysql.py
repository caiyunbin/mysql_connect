# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 16:28:46 2019

@author: caiyu
"""
import pymysql

'''
创建数据库
db=pymysql.connect(host='localhost',
                   user='root',
                   password='caiyunbin3344',
                   port=3306,
                   charset='utf8')
sql='create database test character set utf8'
cursor=db.cursor()
cursor.execute(sql)
'''

db=pymysql.connect(host='localhost',
                   user='root',
                   password='caiyunbin3344',
                   port=3306,
                   db='test',
                   charset='utf8')

cursor=db.cursor()

sql_command='''CREATE TABLE TEST(
             NAME VARCHAR(20) NOT NULL,
             Nickname CHAR(20),
             Age INT,
             SEX CHAR(1),
             Income FLOAT)'''
cursor.execute(sql_command)

cursor=db.cursor()
sql_insert="insert into text(NAME,Nickname,Age,SEX,Income) VALUES('张三','张三疯',15,女,1000)"

try:
        cursor.exexute(sql_insert)
        db.commit()
except Exception as e:
        db.rollback()
finally:
        db.close





