# from django.shortcuts import render, redirect, get_object_or_404
# from .models import *
# from django.contrib.auth.models import User
# # Create your views here.

<<<<<<< HEAD
# def show(request, id):
#     lessons = get_object_or_404(Order, pk=id)
#     return render(request, 'lessons/show.html', {"lessons": lessons})
=======
# Create your views here.

def home(request):
    return render(request, 'home.html')
>>>>>>> d1a6b823dc4e79ad401774708efbc4a1f214ca5e
