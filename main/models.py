from django.db import models
from django.utils import timezone


# Create your models here.
def get_cohort():
    currtime = timezone.now()
    cohort = currtime.strftime("%B-%Y")   
    return cohort   

class Student(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=15)
    dob = models.CharField(max_length=24)
    cohort = models.CharField(max_length=25, default=get_cohort())
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=300)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="books")
    author = models.CharField(max_length=30)
    body = models.TextField()
    isbn = models.CharField(max_length=15, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    # student = models.OneToOneField(Student, on_delete=models.CASCADE)


    def __str__(self):
        return self.title