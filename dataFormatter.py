import json
class Food:
	def __init__(self, meal, calories, date):
		self.meal = meal
		self.calories = calories
		self.date = date

	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__,
			sort_keys=True, indent=4)

def formatter(meals):
	listOfMeals = []
	for meal in meals:
		food = Food(meal['meal'], meal['total_calories'], str(meal['date']))
		listOfMeals.append(food)
	return listOfMeals

def serialize(entry):
	listOfMeals = []
	for each in entry:
		one = each.to_JSON()
		listOfMeals.append(one)
	return listOfMeals

