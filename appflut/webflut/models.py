from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Personal_Inform(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line
    sex = models.TextField()
    date_of_birth = models.TextField()
    weight = models.TextField()
    height = models.TextField()

    # YOUR GOALS
    goals = models.TextField()

    # YOUR LIFESTYLE
    active = models.TextField()




class Add_Product(models.Model):
    name = models.TextField()
    calories_in = models.TextField()
    proteins = models.TextField()
    fats = models.TextField()
    carbohydrates = models.TextField()

def get_default_user():
    return User.objects.get_or_create(username='default')[0].id
class Breakfast_Products(models.Model):
    product = models.ForeignKey(Add_Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)


class Lunch_Products(models.Model):
    product = models.ForeignKey(Add_Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)

class Dinner_Products(models.Model):
     product = models.ForeignKey(Add_Product, on_delete=models.CASCADE)
     user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)

class Snack_Products(models.Model):
    product = models.ForeignKey(Add_Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)



class Activities(models.Model):
    name = models.TextField()
    calories_in = models.TextField()
    time = models.TextField()
class Activities_Add(models.Model):
    product = models.ForeignKey(Activities, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    time = models.IntegerField(default=0)