from django.db import models
from users.models import User

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Lesson(TimeStampedModel):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Order(TimeStampedModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}가 {}를 신청함".format(self.student.username, self.lesson.name)
    
    
class Homework(TimeStampedModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Submit(TimeStampedModel):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    # file = models.FileField()
    
    def __str__(self):
        return "{}가 {}숙제를 제춣함".format(self.student.username, self.homework.name)