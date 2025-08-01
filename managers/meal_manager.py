import json
import os
from models.meal import Meal

class MealManager:
    def __init__(self, storage_path="meals.json"):
        self.storage_path = storage_path
        self.meals = []
        self.load_meals()

    def add_meal(self, meal):
        self.meals.append(meal)
        self.save_meals()

    def save_meals(self):
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump([meal.__dict__ for meal in self.meals], f, ensure_ascii=False, indent=2)

    def load_meals(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.meals = [Meal(**item) for item in data]
        else:
            self.meals = []
