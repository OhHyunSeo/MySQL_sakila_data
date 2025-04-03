#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:33:59 2025

@author: oh
"""

import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'AppleGothic'

host = 'localhost'
user = 'root'
password = '0301'
db_name = 'sakila'

conn = pymysql.connect(host = host,
                       user = user,
                       password = password,
                       db = db_name,
                       charset = 'utf8')

cursor = conn.cursor(pymysql.cursors.DictCursor)

query = """
        SELECT * FROM customer;
        """

query = """
        SELECT 
    c.name AS genre,
    AVG(f.length) AS avg_length
FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name;
"""

# execute()로 query실행
cursor.execute(query)

# 결과로 반환된 테이블의 모든 행을 가져오기 : cursor.fetchall()
execute_result = cursor.fetchall()

# 데이터 프레임
execute_df_length = pd.DataFrame(execute_result)

execute_df_length.head()

plt.figure(figsize=(20, 4))

ax = sns.barplot(x="genre", y="avg_length", data=execute_df_length)

plt.xlabel("장르")
plt.ylabel("평균 상영시간")

plt.ylim(100,)

for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2,  # x 좌표 (막대의 중앙)
            p.get_height() + 0.5,  # y 좌표 (막대 위 약간 위)
            f"{p.get_height():.1f}",  # 표시할 값 (소수점 1자리)
            ha='center', va='bottom', fontsize=12, color='black')

# -----------------------------------------------------------------
query = """
        SELECT
  c.name AS genre, f.rating, COUNT(*) AS rating_count,
  COUNT(*) / (
    SELECT COUNT(*)
    FROM film f2
        JOIN film_category fc2 ON f2.film_id = fc2.film_id
        JOIN category c2 ON fc2.category_id = c2.category_id
    WHERE c2.name = c.name
  ) AS ratio
FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name, f.rating;
"""
# execute()로 query실행
cursor.execute(query)

# 결과로 반환된 테이블의 모든 행을 가져오기 : cursor.fetchall()
execute_result = cursor.fetchall()

# 데이터 프레임
rating = pd.DataFrame(execute_result)

rating.head()

rating.dtypes
rating["ratio"] = rating["ratio"].astype(float)

# 피벗 테이블 생성 (장르별 등급 비율)
pivot_table = rating.pivot_table(index="genre", columns="rating", values="ratio")

# 히트맵 생성
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap="Blues", linewidths=0.5)

# 그래프 제목 및 라벨 설정
plt.title("장르별 등급 비율 히트맵", fontsize=14)
plt.xlabel("영화 등급", fontsize=12)
plt.ylabel("장르", fontsize=12)

# 피벗 테이블 생성 (장르별 rating 분포)
pivot_df = rating.pivot(index="genre", columns="rating", values="ratio")

# Stacked Bar Plot
pivot_df.plot(kind="bar", stacked=True, figsize=(12, 6), colormap="viridis")

# 그래프 꾸미기
plt.xlabel("장르")
plt.ylabel("비율 (ratio)")
plt.title("장르별 등급 분포")
plt.legend(title="Rating")
plt.xticks(rotation=45)  # X축 라벨 회전

#--------------------------------
query = """
        SELECT
  cat.name AS genre,
  COUNT(*) AS rental_count
FROM rental r
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film f ON i.film_id = f.film_id
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category cat ON fc.category_id = cat.category_id
    JOIN customer cust ON r.customer_id = cust.customer_id
GROUP BY cat.name
ORDER BY rental_count DESC;
"""
# execute()로 query실행
cursor.execute(query)

# 결과로 반환된 테이블의 모든 행을 가져오기 : cursor.fetchall()
execute_result = cursor.fetchall()

# 데이터 프레임
rental_count = pd.DataFrame(execute_result)

rental_count.head()

plt.figure(figsize=(20, 4))

ax = sns.barplot(x="genre", y="rental_count", data=rental_count)

plt.xlabel("장르")
plt.ylabel("대여 회수")

plt.ylim(800,)

for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2,  # x 좌표 (막대의 중앙)
            p.get_height() + 0.5,  # y 좌표 (막대 위 약간 위)
            f"{p.get_height():.1f}",  # 표시할 값 (소수점 1자리)
            ha='center', va='bottom', fontsize=12, color='black')










