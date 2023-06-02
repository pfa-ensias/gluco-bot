import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
import csv
import django
django.setup()


from diabetes.models import Exercisecalorie, Food
with open('./data/exercise_calories.csv') as csvfile:

    reader = csv.DictReader(csvfile)
    for row in reader:
        exercise = Exercisecalorie.objects.create(
            exercisename=row['exercisename'],
            metvalue=row['metvalue'],
            note=row['note']

        )
        exercise.save()

with open('./data/food_calories.csv') as csvfile:

    reader = csv.DictReader(csvfile)
    for row in reader:
        food = Food.objects.create(
            name=row['FoodItem'],
            calories=row['Calper100g'],

        )
        food.save()


