from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_year = models.IntegerField()
    address = models.CharField(max_length=200, default='')
    grade = models.CharField(max_length=10, default='A')
    def __str__(self):
        return self.title
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    published_year = models.IntegerField()

    def __str__(self):
        return self.title


class AjaySchool(models.Model):
    name = models.CharField(max_length=100)
    published_year = models.IntegerField()

    def __str__(self):
        return self.title
    


class New_changes(models.Model):
    name = models.CharField(max_length=100)
    published_year = models.IntegerField()
    address = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.title


