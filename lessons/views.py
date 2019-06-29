from django.shortcuts import render, redirect, get_object_or_404
# from .models import *
# from django.contrib.auth.models import User
# # Create your views here.

<<<<<<< HEAD

def show(request, id):
    lessons = get_object_or_404(Order, pk=id)
    return render(request, 'lessons/show.html', {"lessons": lessons})

def home(request):
    return render(request, 'home.html')

=======
# def show(request, id):
#     lessons = get_object_or_404(Order, pk=id)
#     return render(request, 'lessons/show.html', {"lessons": lessons})
# Create your views here.

def first(request):
    return render(request, 'first.html')
>>>>>>> d7cbf4ee4fed7aa40874c6b3f387e807bd043325
