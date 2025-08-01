import requests
from bs4 import BeautifulSoup
import re

class FoodInfoScraper:
    def __init__(self):
        self.search_url = "https://search.naver.com/search.naver"

    def get_calories(self, food_name):
        params = {
            "query": f"{food_name} 칼로리"
        }

        try:
            response = requests.get(self.search_url, params=params, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            # 칼로리 정보가 포함된 텍스트 찾기
            possible_tags = soup.find_all(string=re.compile(r"\d+\.?\d*\s?kcal"))

            for tag in possible_tags:
                match = re.search(r"(\d+\.?\d*)\s?kcal", tag)
                if match:
                    return float(match.group(1))

            print("⚠️ 칼로리 정보를 찾을 수 없습니다.")
            return 0.0

        except Exception as e:
            print(f"❌ 오류 발생: {e}")
            return 0.0
