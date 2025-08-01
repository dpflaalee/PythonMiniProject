from managers.meal_manager import MealManager
from models.meal import Meal
from utils.food_scraper import FoodInfoScraper
from utils.visualizer import plot_daily_calories
from datetime import datetime

def main():
    manager = MealManager()
    scraper = FoodInfoScraper()

    while True:
        print("\n🍽️ 식단 관리 시스템")
        print("1. 식사 기록 추가")
        print("2. 식단 조회")
        print("3. 칼로리 분석")
        print("4. 칼로리 시각화")
        print("5. 종료")

        choice = input("선택 >> ")

        if choice == "1":
            name = input("음식 이름: ")
            meal_type = input("식사 종류 (아침/점심/저녁/간식): ")
            date = input("날짜 (YYYY-MM-DD, 빈칸이면 오늘): ")
            if not date:
                date = datetime.now().strftime("%Y-%m-%d")

            # 칼로리 자동 크롤링
            calories = scraper.get_calories(name)
            print(f"✔️ '{name}'의 예상 칼로리: {calories} kcal")

            meal = Meal(date, name, calories, meal_type)
            manager.add_meal(meal)
            print("✅ 식사 기록이 추가되었습니다.")

        elif choice == "2":
            date = input("조회할 날짜 (YYYY-MM-DD, 빈칸이면 전체): ")
            meals = manager.meals if not date else [m for m in manager.meals if m.date == date]
            if meals:
                print(f"\n📋 식단 조회 결과 ({date if date else '전체'})")
                for m in meals:
                    print(f"- {m.date} | {m.meal_type} | {m.name} | {m.calories} kcal")
            else:
                print("❌ 해당 날짜의 식단 기록이 없습니다.")

        elif choice == "3":
            total = sum(m.calories for m in manager.meals)
            avg = total / len(manager.meals) if manager.meals else 0
            print(f"\n📊 총 칼로리: {total:.2f} kcal")
            print(f"📈 평균 칼로리: {avg:.2f} kcal")

        elif choice == "4":
            plot_daily_calories(manager.meals)

        elif choice == "5":
            print("👋 프로그램을 종료합니다.")
            break

        else:
            print("❗ 유효한 메뉴 번호를 입력해주세요.")

if __name__ == "__main__":
    main()
1
