from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from lessons .models import *
# Create your views here.


<<<<<<< HEAD
=======
def classes(request):
    return render(request, 'classes.html')

>>>>>>> d7cbf4ee4fed7aa40874c6b3f387e807bd043325
def home(request, id):
    user = get_object_or_404(User, pk=id)
    lessonsOfTeacher = Lesson.objects.all()
    lessonsOfStudent = Order.objects.all()
    return render(request, 'home.html', {'user': user, 'lessonsOfTeacher': lessonsOfTeacher, 'lessonsOfStudent': lessonsOfStudent})
<<<<<<< HEAD
=======

>>>>>>> d7cbf4ee4fed7aa40874c6b3f387e807bd043325
