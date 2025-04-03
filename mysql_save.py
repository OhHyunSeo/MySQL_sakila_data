#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:01:30 2025

@author: oh
"""


import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sqlalchemy import create_engine

pymysql.install_as_MySQLdb()
import MySQLdb

host = 'localhost'
user = 'root'
password = '0301'
db_name = 'testdb'
charset = 'utf8'


# 데이터 불러오기
jan = pd.read_csv("./data/2024년 1월 국내노선 여객 이용률.csv")

feb = pd.read_csv("./data/2024년 2월 국내노선 여객 이용률.csv")

mar = pd.read_csv("./data/2024년 3월 국내노선 여객 이용률.csv")

apr = pd.read_csv("./data/2024년 4월 국내노선 여객 이용률.csv")

may = pd.read_csv("./data/2024년 5월 국내노선 여객 이용률.csv")

jun = pd.read_csv("./data/2024년 6월 국내노선 여객 이용률.csv")

jul = pd.read_csv("./data/2024년 7월 국내노선 여객 이용률.csv")

aug = pd.read_csv("./data/2024년 8월 국내노선 여객 이용률.csv")

montly_passengers = pd.read_csv("./data/한국공항공사_국내노선 여객 월별 이용률_20250131.csv")

dom_sch = pd.read_csv("./data/한국공항공사_국내선 항공기스케줄_20160512..csv")

int_sch = pd.read_csv("./data/한국공항공사_국제선 항공기스케줄_20150323.csv")

# 각 월별 데이터 별 결측치 파악
jan.isna().sum() # 없음

feb.isna().sum() # 없음

mar.isna().sum() # 없음

apr.isna().sum()
'''
노선     0
항공사    0
좌석수    0
성인     0
유아     2
여객수    0
이용률    0
dtype: int64
'''

may.isna().sum() # 없음

jun.isna().sum() # 없음

jul.isna().sum() # 없음

aug.isna().sum() # 없음

# 4월 데이터에서 결측치 발견
# 결측치 처리 -> 중앙값으로 대체
apr['유아'].mean() # 248.93457943925233
apr['유아'].median() # 146.0


apr['유아'] = apr['유아'].fillna(apr['유아'].median())

apr.isna().sum()
# 처리 완료

# 1월달의 항공사명을 영어코드로 변환
# 항공사명에 항공사 코드를 매핑

airline_mapping = {
    "대한항공": "KAL",
    "제주항공": "JJA",
    "아시아나": "AAR",
    "이스타항공": "ESR",
    "티웨이항공": "TWB",
    "에어부산": "ABL",
    "진에어": "JNA",
    "에어서울": "ASV",
    "에어로케이": "EOK"
}

jan["항공사"] = jan["항공사"].map(airline_mapping)


# 1월 분 시각화

plt.rcParams['font.family'] = 'AppleGothic'

jan.info()


# 이용률 변수 설정
usage_rates = jan.groupby("노선")["이용율"].mean().reset_index()

#이용률이 높은 상위 5개 노선 찾기
jan_top_5_routes = usage_rates.sort_values(by="이용율", ascending=False).head(5)

# 결과 출력
print(jan_top_5_routes)
'''
       노선      이용율
31  제주-울산  96.1000
26  제주-김포  93.8125
28  제주-대구  93.5800
8   김포-제주  93.0875
20  울산-제주  92.7000
'''

plt.figure(figsize=(8, 5))
sns.barplot(data=jan_top_5_routes, x="이용율", y="노선", palette="Reds_r")

plt.xlabel("이용률 (%)")
plt.ylabel("노선")
plt.title("1 월 이용률이 높은 상위 5개 노선")
plt.xlim(92, 97)


#--------------------
# 2월 분 시각화

feb_usage_rates = feb.groupby("노선")["이용율"].mean().reset_index()


#이용률이 높은 상위 5개 노선 찾기
feb_top_5_routes = feb_usage_rates.sort_values(by="이용율", ascending=False).head(5)

# 결과 출력
print(feb_top_5_routes)
'''
        노선      이용율
32  제주-울산   95.0000
9    김포-제주  93.4125
8    김포-인천  93.1000
27   제주-김포  92.9500
21   울산-제주  91.1000
'''

plt.figure(figsize=(8, 5))
sns.barplot(data= feb_top_5_routes, x="이용율", y="노선", palette="Reds_r")

plt.xlabel("이용률 (%)")
plt.ylabel("노선")
plt.title("2 월 이용률이 높은 상위 5개 노선")
plt.xlim(91, 96)

#--------------------
# 3월 분 시각화

mar_usage_rates = mar.groupby("노선")["이용률"].mean().reset_index()


#이용률이 높은 상위 5개 노선 찾기
mar_top_5_routes = mar_usage_rates.sort_values(by="이용률", ascending=False).head(5)

# 결과 출력
print(mar_top_5_routes)
'''
       노선    이용률
26  제주-김포  91.25
8   김포-제주  91.15
10  김해-김포  89.50
4   김포-김해  88.34
12  김해-제주  86.10
'''

plt.figure(figsize=(8, 5))
sns.barplot(data= mar_top_5_routes, x="이용률", y="노선", palette="Reds_r")

plt.xlabel("이용률 (%)")
plt.ylabel("노선")
plt.title("3 월 이용률이 높은 상위 5개 노선")
plt.xlim(85, 93)

#--------------------
# 4월 분 시각화

apr_usage_rates = apr.groupby("노선")["이용률"].mean().reset_index()


#이용률이 높은 상위 5개 노선 찾기
apr_top_5_routes = apr_usage_rates.sort_values(by="이용률", ascending=False).head(5)

# 결과 출력
print(apr_top_5_routes)
'''
       노선        이용률
27  제주-김포  95.125000
12  김해-제주  94.825000
8   김포-제주  93.175000
28  제주-김해  92.150000
38  청주-제주  91.171429
'''

plt.figure(figsize=(8, 5))
sns.barplot(data= apr_top_5_routes, x="이용률", y="노선", palette="Reds_r")

plt.xlabel("이용률 (%)")
plt.ylabel("노선")
plt.title("4 월 이용률이 높은 상위 5개 노선")
plt.xlim(90, 96)

#--------------------
# 5월 분 시각화

may_usage_rates = may.groupby("노선")["이용률"].mean().reset_index()


#이용률이 높은 상위 5개 노선 찾기
may_top_5_routes = may_usage_rates.sort_values(by="이용률", ascending=False).head(5)

# 결과 출력
print(may_top_5_routes)
'''
       노선        이용률
27  제주-김포  95.225000
8   김포-제주  94.537500
12  김해-제주  93.975000
4   김포-김해  91.750000
38  청주-제주  91.557143
'''

plt.figure(figsize=(8, 5))
sns.barplot(data= may_top_5_routes, x="이용률", y="노선", palette="Reds_r")

plt.xlabel("이용률 (%)")
plt.ylabel("노선")
plt.title("5 월 이용률이 높은 상위 5개 노선")
plt.xlim(90, 96)

#--------------------
# 6월 분 시각화

jun_usage_rates = jun.groupby("노선")["이용률"].mean().reset_index()


#이용률이 높은 상위 5개 노선 찾기
jun_top_5_routes = jun_usage_rates.sort_values(by="이용률", ascending=False).head(5)

# 결과 출력
print(jun_top_5_routes)
'''
       노선        이용률
27  제주-김포  94.625000
36  제주-청주  92.014286
8   김포-제주  91.850000
38  청주-제주  90.328571
4   김포-김해  89.950000
'''

plt.figure(figsize=(8, 5))
sns.barplot(data= jun_top_5_routes, x="이용률", y="노선", palette="Reds_r")

plt.xlabel("이용률 (%)")
plt.ylabel("노선")
plt.title("6 월 이용률이 높은 상위 5개 노선")
plt.xlim(89, 96)

#--------------------
# 7월 분 시각화

jul_usage_rates = jul.groupby("노선")["이용률"].mean().reset_index()


#이용률이 높은 상위 5개 노선 찾기
jul_top_5_routes = jul_usage_rates.sort_values(by="이용률", ascending=False).head(5)

# 결과 출력
print(jul_top_5_routes)
'''
       노선        이용률
8   김포-제주  94.037500
38  청주-제주  90.942857
27  제주-김포  90.912500
4   김포-김해  87.866667
12  김해-제주  87.000000
'''

plt.figure(figsize=(8, 5))
sns.barplot(data= jul_top_5_routes, x="이용률", y="노선", palette="Reds_r")

plt.xlabel("이용률 (%)")
plt.ylabel("노선")
plt.title("7 월 이용률이 높은 상위 5개 노선")
plt.xlim(85, 95)


#--------------------
# 8월 분 시각화

aug_usage_rates = aug.groupby("노선")["이용률"].mean().reset_index()


#이용률이 높은 상위 5개 노선 찾기
aug_top_5_routes = aug_usage_rates.sort_values(by="이용률", ascending=False).head(5)

# 결과 출력
print(aug_top_5_routes)
'''
       노선        이용률
37  제주-청주  96.514286
28  제주-김포  95.712500
29  제주-김해  94.100000
39  청주-제주  93.571429
13  김해-제주  93.500000
'''

plt.figure(figsize=(8, 5))
sns.barplot(data= aug_top_5_routes, x="이용률", y="노선", palette="Reds_r")

plt.xlabel("이용률 (%)")
plt.ylabel("노선")
plt.title("8 월 이용률이 높은 상위 5개 노선")
plt.xlim(92, 97)

# --------------------------------------------
# 1워 인기 노선 별 항공사들의 점유율 시각화

# ["노선"]의 공백 제거
jan["노선"] = jan["노선"].str.strip()

selected_df = jan[jan["노선"].isin(jan_top_5_routes["노선"])]

# 점유율(%) 계산
total_passengers = selected_df.groupby("노선")["여객수"].sum().reset_index()
airline_passengers = selected_df.groupby(["노선", "항공사"])["여객수"].sum().reset_index()

merged_df = airline_passengers.merge(total_passengers, on="노선", suffixes=("", "_total"))
merged_df["점유율(%)"] = (merged_df["여객수"] / merged_df["여객수_total"]) * 100

# 시각화
plt.figure(figsize=(10, 6))
sns.barplot(
    data=merged_df, 
    x="노선", 
    y="점유율(%)", 
    hue="항공사", 
    palette="Set2"
)

# 그래프 설정
plt.title("1월 인기 노선별 항공사 점유율", fontsize=14)
plt.xlabel("노선")
plt.ylabel("점유율 (%)")
plt.xticks(rotation=45)
plt.legend(title="항공사")
plt.show()

# --------------------------------------------
# 2월 인기 노선 별 항공사들의 점유율 시각화

# ["노선"]의 공백 제거
feb["노선"] = feb["노선"].str.strip()

selected_df = feb[feb["노선"].isin(feb_top_5_routes["노선"])]

# 점유율(%) 계산
total_passengers = selected_df.groupby("노선")["여객수"].sum().reset_index()
airline_passengers = selected_df.groupby(["노선", "항공사"])["여객수"].sum().reset_index()

merged_df = airline_passengers.merge(total_passengers, on="노선", suffixes=("", "_total"))
merged_df["점유율(%)"] = (merged_df["여객수"] / merged_df["여객수_total"]) * 100

# 시각화
plt.figure(figsize=(10, 6))
sns.barplot(
    data=merged_df, 
    x="노선", 
    y="점유율(%)", 
    hue="항공사", 
    palette="Set2"
)

# 그래프 설정
plt.title("2월 인기 노선별 항공사 점유율", fontsize=14)
plt.xlabel("노선")
plt.ylabel("점유율 (%)")
plt.xticks(rotation=45)
plt.legend(title="항공사")
plt.show()

# --------------------------------------------
# 3월 인기 노선 별 항공사들의 점유율 시각화

# ["노선"]의 공백 제거
mar["노선"] = mar["노선"].str.strip()

selected_df = mar[mar["노선"].isin(mar_top_5_routes["노선"])]

# 점유율(%) 계산
total_passengers = selected_df.groupby("노선")["여객수"].sum().reset_index()
airline_passengers = selected_df.groupby(["노선", "항공사"])["여객수"].sum().reset_index()

merged_df = airline_passengers.merge(total_passengers, on="노선", suffixes=("", "_total"))
merged_df["점유율(%)"] = (merged_df["여객수"] / merged_df["여객수_total"]) * 100

# 시각화
plt.figure(figsize=(10, 6))
sns.barplot(
    data=merged_df, 
    x="노선", 
    y="점유율(%)", 
    hue="항공사", 
    palette="Set2"
)

# 그래프 설정
plt.title("3월 인기 노선별 항공사 점유율", fontsize=14)
plt.xlabel("노선")
plt.ylabel("점유율 (%)")
plt.xticks(rotation=45)
plt.legend(title="항공사")
plt.show()

# --------------------------------------------
# 4월 인기 노선 별 항공사들의 점유율 시각화

# ["노선"]의 공백 제거
apr["노선"] = apr["노선"].str.strip()

selected_df = apr[apr["노선"].isin(apr_top_5_routes["노선"])]

# 점유율(%) 계산
total_passengers = selected_df.groupby("노선")["여객수"].sum().reset_index()
airline_passengers = selected_df.groupby(["노선", "항공사"])["여객수"].sum().reset_index()

merged_df = airline_passengers.merge(total_passengers, on="노선", suffixes=("", "_total"))
merged_df["점유율(%)"] = (merged_df["여객수"] / merged_df["여객수_total"]) * 100

# 시각화
plt.figure(figsize=(10, 6))
sns.barplot(
    data=merged_df, 
    x="노선", 
    y="점유율(%)", 
    hue="항공사", 
    palette="Set2"
)

# 그래프 설정
plt.title("4월 인기 노선별 항공사 점유율", fontsize=14)
plt.xlabel("노선")
plt.ylabel("점유율 (%)")
plt.xticks(rotation=45)
plt.legend(title="항공사")
plt.show()

# --------------------------------------------
# 5월 인기 노선 별 항공사들의 점유율 시각화

# ["노선"]의 공백 제거
may["노선"] = may["노선"].str.strip()

selected_df = may[may["노선"].isin(jan_top_5_routes["노선"])]

# 점유율(%) 계산
total_passengers = selected_df.groupby("노선")["여객수"].sum().reset_index()
airline_passengers = selected_df.groupby(["노선", "항공사"])["여객수"].sum().reset_index()

merged_df = airline_passengers.merge(total_passengers, on="노선", suffixes=("", "_total"))
merged_df["점유율(%)"] = (merged_df["여객수"] / merged_df["여객수_total"]) * 100

# 시각화
plt.figure(figsize=(10, 6))
sns.barplot(
    data=merged_df, 
    x="노선", 
    y="점유율(%)", 
    hue="항공사", 
    palette="Set2"
)

# 그래프 설정
plt.title("5월 인기 노선별 항공사 점유율", fontsize=14)
plt.xlabel("노선")
plt.ylabel("점유율 (%)")
plt.xticks(rotation=45)
plt.legend(title="항공사")
plt.show()

# --------------------------------------------
# 6월 인기 노선 별 항공사들의 점유율 시각화

# ["노선"]의 공백 제거
jun["노선"] = jun["노선"].str.strip()

selected_df = jun[jun["노선"].isin(jun_top_5_routes["노선"])]

# 점유율(%) 계산
total_passengers = selected_df.groupby("노선")["여객수"].sum().reset_index()
airline_passengers = selected_df.groupby(["노선", "항공사"])["여객수"].sum().reset_index()

merged_df = airline_passengers.merge(total_passengers, on="노선", suffixes=("", "_total"))
merged_df["점유율(%)"] = (merged_df["여객수"] / merged_df["여객수_total"]) * 100

# 시각화
plt.figure(figsize=(10, 6))
sns.barplot(
    data=merged_df, 
    x="노선", 
    y="점유율(%)", 
    hue="항공사", 
    palette="Set2"
)

# 그래프 설정
plt.title("6월 인기 노선별 항공사 점유율", fontsize=14)
plt.xlabel("노선")
plt.ylabel("점유율 (%)")
plt.xticks(rotation=45)
plt.legend(title="항공사")
plt.show()

# --------------------------------------------
# 7월 인기 노선 별 항공사들의 점유율 시각화

# ["노선"]의 공백 제거
jul["노선"] = jul["노선"].str.strip()

selected_df = jul[jul["노선"].isin(jul_top_5_routes["노선"])]

# 점유율(%) 계산
total_passengers = selected_df.groupby("노선")["여객수"].sum().reset_index()
airline_passengers = selected_df.groupby(["노선", "항공사"])["여객수"].sum().reset_index()

merged_df = airline_passengers.merge(total_passengers, on="노선", suffixes=("", "_total"))
merged_df["점유율(%)"] = (merged_df["여객수"] / merged_df["여객수_total"]) * 100

# 시각화
plt.figure(figsize=(10, 6))
sns.barplot(
    data=merged_df, 
    x="노선", 
    y="점유율(%)", 
    hue="항공사", 
    palette="Set2"
)

# 그래프 설정
plt.title("7월 인기 노선별 항공사 점유율", fontsize=14)
plt.xlabel("노선")
plt.ylabel("점유율 (%)")
plt.xticks(rotation=45)
plt.legend(title="항공사")
plt.show()

# --------------------------------------------
# 8월 인기 노선 별 항공사들의 점유율 시각화

# ["노선"]의 공백 제거
aug["노선"] = aug["노선"].str.strip()

selected_df = aug[aug["노선"].isin(aug_top_5_routes["노선"])]

# 점유율(%) 계산
total_passengers = selected_df.groupby("노선")["여객수"].sum().reset_index()
airline_passengers = selected_df.groupby(["노선", "항공사"])["여객수"].sum().reset_index()

merged_df = airline_passengers.merge(total_passengers, on="노선", suffixes=("", "_total"))
merged_df["점유율(%)"] = (merged_df["여객수"] / merged_df["여객수_total"]) * 100

# 시각화
plt.figure(figsize=(10, 6))
sns.barplot(
    data=merged_df, 
    x="노선", 
    y="점유율(%)", 
    hue="항공사", 
    palette="Set2"
)

# 그래프 설정
plt.title("8월 인기 노선별 항공사 점유율", fontsize=14)
plt.xlabel("노선")
plt.ylabel("점유율 (%)")
plt.xticks(rotation=45)
plt.legend(title="항공사")
plt.show()
# -------- mysql 저장
engine = create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{db_name}")

conn = engine.connect()

jan.to_sql(name = 'January', con = engine, if_exists = 'replace', index = False)

feb.to_sql(name = 'February', con = engine, if_exists = 'replace', index = False)

mar.to_sql(name = 'March', con = engine, if_exists = 'replace', index = False)

apr.to_sql(name = 'April', con = engine, if_exists = 'replace', index = False)

may.to_sql(name = 'May', con = engine, if_exists = 'replace', index = False)

jun.to_sql(name = 'June', con = engine, if_exists = 'replace', index = False)

jul.to_sql(name = 'July', con = engine, if_exists = 'replace', index = False)

aug.to_sql(name = 'August', con = engine, if_exists = 'replace', index = False)

conn.close()























