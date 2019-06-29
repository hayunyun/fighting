from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from lessons .models import *
# Create your views here.


def classes(request):
    return render(request, 'classes.html')

def home(request, id):
    user = get_object_or_404(User, pk=id)
    lessonsOfTeacher = Lesson.objects.all()
    lessonsOfStudent = Order.objects.all()
    return render(request, 'home.html', {'user': user, 'lessonsOfTeacher': lessonsOfTeacher, 'lessonsOfStudent': lessonsOfStudent})

