# 🥗 Meal Tracker & Calorie Visualizer

식사 기록을 관리하고, 음식의 칼로리 정보를 자동으로 크롤링하여 일별 섭취량을 시각화하는 Python 미니 프로젝트입니다.
---

## 📦 주요 기능

- ✅ 식사 기록 추가 (음식 이름, 날짜, 식사 종류)
- 🔍 네이버 검색을 통한 칼로리 자동 크롤링
- 📊 일별 칼로리 섭취량 시각화 (matplotlib)
- 💾 JSON 파일로 데이터 저장 및 불러오기

---

## 🛠 사용 방법

### 1. 설치

```bash
git clone https://github.com/dpflaalee/PythonMiniProject.git
cd PythonMiniProject
pip install -r requirements.txt
bash

### 2. 실행
```bash
python main.py
bash

### 3. 메뉴 예시
1. 식사 추가
2. 식사 목록 보기
3. 데이터 저장
4. 칼로리 시각화
5. 종료

### 📁 프로젝트 구조
meal-tracker/
├── main.py
├── models/
│   └── meal.py
├── utils/
│   ├── scraper.py
│   └── visualizer.py
├── data/
│   └── meals.json
└── README.md

### 🔍 칼로리 크롤링 방식
네이버 검색 결과에서 "{음식 이름} 칼로리"로 검색

HTML에서 "123 kcal" 형태의 텍스트를 정규식으로 추출

실패 시 0.0 kcal로 처리

### 📊 시각화 예시
matplotlib를 사용하여 날짜별 섭취 칼로리를 선 그래프로 표시

### 추후 Pie Chart, Bar Chart 등으로 확장 가능

### 📌 요구사항
Python 3.8+

requests, beautifulsoup4, matplotlib, pandas


pip install requests beautifulsoup4 matplotlib pandas
