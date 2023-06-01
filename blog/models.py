from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


# Create your models here.
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
    
class Post(models.Model):
    title = models.CharField(max_length= 100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add= True)
    published_at = models.DateField(null= True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    year = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    
class Question(models.Model):
    question_text = models.CharField(max_length= 200)
    publish_date = models.DateTimeField( 'date published' )

    def was_published_recently(self):
        return (self.publish_date < timezone.now() and
                self.publish_date >= timezone.now() - datetime.timedelta(days= 1))

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length= 200)
    votes = models.IntegerField(default= 0)