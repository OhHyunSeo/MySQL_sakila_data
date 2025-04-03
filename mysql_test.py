#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:53:50 2025

@author: oh

mysql 연동
"""

# pip install pymysql

import pymysql
import pandas as pd

host = 'localhost'
user = 'root'
password = '0301'
db_name = 'sakila'

# 접속 : pymysql.connect()
# host : 접속주소 (ip)
# user : 사용자 아이디
# password : 비밀번호
# db = 데이터베이스
# charset = 인코딩

conn = pymysql.connect(host = host,
                       user = user,
                       password = password,
                       db = db_name,
                       charset = 'utf8')

# 커서 생성 : query를 실행하는 execute()
# key-value => DictCursor

cursor = conn.cursor(pymysql.cursors.DictCursor)

query = """
        SELECT * FROM customer;
        """
        
# execute()로 query실행
cursor.execute(query)

# 결과로 반환된 테이블의 모든 행을 가져오기 : cursor.fetchall()
execute_result = cursor.fetchall()

# 데이터 프레임
execute_df = pd.DataFrame(execute_result)

# DB 연결 종료
conn.close()




























