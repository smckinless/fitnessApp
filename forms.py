from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired

class FoodForm(Form):
	meal = TextField('meal', validators=[DataRequired()])
	total_calories = TextField('total_calories', validators=[DataRequired()])

class WorkoutForm(Form):
	reps = TextField('reps')
	length = TextField('length')