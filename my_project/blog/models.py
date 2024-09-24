from django.db import models


class Bag(models.Model):
    brand = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    color = models.CharField(max_length=256)
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.brand} {self.model}'
    

class Phone(models.Model):
    title = models.CharField(max_length=256)
    color = models.CharField(max_length=256)
    year = models.IntegerField()
    price = models.IntegerField()
     
    def __str__(self) -> str:
        return f'{self.title} {self.year}'
     
     
class Animal(models.Model): 
    species = models.CharField(max_length=256)
    color = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.species} {self.color}'
    
    
class Car(models.Model):
    brand = models.CharField(max_length=256)
    color = models.CharField(max_length=256)
    year = models.IntegerField()
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.brand} {self.color}'
    
    
class Book(models.Model):
    name = models.CharField(max_length=256)
    publisher = models.CharField(max_length=256)
    year = models.IntegerField()    
    author = models.CharField(max_length=256)
    
    def __str__(self) -> str:
        return f'{self.name} {self.author}'