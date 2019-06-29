from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from lessons .models import *
# Create your views here.

<<<<<<< HEAD
def home(request, id):
    user = get_object_or_404(User, pk=id)
    lessonsOfTeacher = Lesson.objects.all()
    lessonsOfStudent = Order.objects.all()
    return render(request, 'home.html', {'user': user, 'lessonsOfTeacher': lessonsOfTeacher, 'lessonsOfStudent': lessonsOfStudent})
=======
>>>>>>> d1a6b823dc4e79ad401774708efbc4a1f214ca5e
