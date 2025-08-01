class Meal:
    def __init__(self, date, name, calories, meal_type):
        self.date = date
        self.name = name
        self.calories = calories
        self.meal_type = meal_type

    def to_dict(self):
        return {
            "date": self.date,
            "name": self.name,
            "calories": self.calories,
            "meal_type": self.meal_type
        }
