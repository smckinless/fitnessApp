from flask import Flask, render_template, request
import pymongo
from pymongo import MongoClient
import datetime
from dataFormatter import *
from exporter import *

client = MongoClient('mongodb://admin:myfitnessapp2016@ds047065.mongolab.com:47065/myfitness')
db = client.myfitness
collection_food = db.food
collection_workout = db.workout


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/fitness', methods=['GET', 'POST'])
def fitness():
	return render_template('fitness.html')

@app.route('/workouts', methods=['GET', 'POST'])
def workouts():


	#form = WorkoutForm()
	return render_template('workouts.html')

@app.route('/food', methods=['GET', 'POST'])
def food():
	#form = FoodForm(request.form)
	listOfMeals = []
	meals = collection_food.find()
	listOfMeals = formatter(meals)
	listOfCalories = exporter(listOfMeals, 'total_calories')
	listOfEatenMeals = exporter(listOfMeals, 'meal')
	listOfDates = exporter(listOfMeals, 'date')
	if request.method == 'POST':
		date = request.form['date']
		meal = request.form['meal']
		total_calories = request.form['total_calories']
		new_meal = {'meal' : meal,
					'total_calories' : total_calories,
					'date' : date}
		collection_food.insert(new_meal)
		print meals
		return render_template('food.html', listOfDates=listOfDates, listOfEatenMeals=listOfEatenMeals, listOfCalories=listOfCalories,listOfMeals=listOfMeals, meals=meals)
	else:
		print meals
		return render_template('food.html', listOfDates=listOfDates, listOfEatenMeals=listOfEatenMeals, listOfCalories=listOfCalories, listOfMeals=listOfMeals, meals=meals)

if __name__ == '__main__':
	app.run(debug=True)