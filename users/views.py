from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from lessons .models import *
# Create your views here.



def classes(request):
    return render(request, 'classes.html')



@login_required
def home(request):
    user = request.user
    if user.state == 'Teacher':
        lessons = Lesson.objects.filter(teacher=user)
    else:
        lessons = Order.objects.filter(student=user)
    return render(request, 'home.html', {'user': user, 'lessons': lessons})






