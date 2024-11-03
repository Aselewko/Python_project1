from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    students_qwt = models.IntegerField()
    reviews_qwt = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title + ' ' + str(self.students_qwt)