from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Appointment(models.Model):
    class Meta:
        db_table = 'appointment'
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    hospital = models.CharField(max_length=120)
    provider = models.CharField(max_length=120)
    appointmenttime = models.DateTimeField()


class Food(models.Model):
    class Meta:
        db_table = 'food'

    name = models.CharField(max_length=100)
    calories = models.IntegerField()


    def __str__(self):
        return self.name

class Diet(models.Model):
    class Meta:
        db_table = 'diet'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    recordtime = models.DateTimeField()

    def calories(self):
        return self.food.calories * self.quantity



class Bloodsugar(models.Model):
    class Meta:
        db_table = 'bloodsugar'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    bloodsugarmeasure = models.DecimalField(max_digits=5, decimal_places=2)
    measuretime = models.DateTimeField()



class Weight(models.Model):
    class Meta:
        db_table = 'weight'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    weight = models.CharField(max_length=500) ## Changed from 120 to 500
    measuretime = models.DateTimeField()





class Exercisecalorie(models.Model):
    class Meta:
        db_table = 'excercisecalorie'

    exercisename = models.CharField(max_length=100)
    metvalue = models.FloatField()
    note = models.TextField(max_length=200)
    
    def __str__(self) -> str:
        return self.exercisename



class Exercise(models.Model):
    class Meta:
        db_table = 'exercise'

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    exercise = models.ForeignKey(Exercisecalorie, on_delete=models.CASCADE)
    #exercisedate = models.DateTimeField(auto_now_add=True)
    exercisedate = models.DateTimeField()
    currentweight = models.FloatField()
    updated = models.DateTimeField(auto_now=True)
    hour = models.FloatField()
    totalcalories = models.FloatField(null=True)
    """
    def totalcalories(self):
        return  self.exercise.metvalue * self.currentweight * self.hour
    """
    
    def save(self, *args, **kwargs):
        self.totalcalories = self.exercise.metvalue * self.currentweight * self.hour
        super(Exercise, self).save(*args, **kwargs)
    

