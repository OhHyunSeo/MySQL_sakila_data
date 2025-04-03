# 🎬 MySQL Sakila DVD Rental Data Project

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/Database-MySQL-lightblue.svg)](https://www.mysql.com/)

## 🔍 소개

이 프로젝트는 **MySQL Sakila** 샘플 데이터베이스를 기반으로, DVD 대여 시스템의 데이터를 분석하고  
Python을 통해 MySQL 데이터베이스에 접근하여 저장, 조회, 분석하는 기능을 구현합니다.

---

## 🧩 주요 기능

- 📦 Sakila DVD 대여 샘플 데이터 활용
- 🗄️ Python으로 MySQL 연결 및 데이터 저장
- 🔍 간단한 쿼리 분석 및 테스트 수행

---

## 📁 프로젝트 구조

```
📁 MySQL_sakila_data-master/
│
├── DVD_tp.py         # DVD 대여 및 관련 데이터 분석 처리
├── mysql_save.py     # MySQL로 데이터 저장/삽입 기능 구현
└── mysql_test.py     # MySQL 연결 및 쿼리 테스트 코드
```

---

## 🚀 실행 방법

### 1. MySQL 설치 및 Sakila DB 로드

- [Sakila Sample Database](https://dev.mysql.com/doc/sakila/en/)를 설치하세요.
- 아래 명령어로 데이터베이스를 임포트합니다:

```bash
mysql -u root -p < sakila-schema.sql
mysql -u root -p < sakila-data.sql
```

### 2. Python 환경 설정

```bash
python -m venv venv
source venv/bin/activate
pip install mysql-connector-python
```

### 3. 코드 실행 예시

```bash
python mysql_test.py     # MySQL 연결 테스트
python mysql_save.py     # 데이터 저장 수행
python DVD_tp.py         # DVD 대여 관련 데이터 분석
```

---

## 💾 요구 사항

- Python 3.9 이상
- MySQL 서버 실행 환경
- mysql-connector-python

---

## 🧑‍💻 기여 방법

1. 이 레포지토리를 포크합니다.
2. 새 브랜치를 생성하세요: `git checkout -b feature/기능명`
3. 커밋하세요: `git commit -m "Add 기능"`
4. 브랜치에 푸시하세요: `git push origin feature/기능명`
5. Pull Request를 생성하세요.
