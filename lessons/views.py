from django.shortcuts import render, redirect, get_object_or_404
# from .models import *
# from django.contrib.auth.models import User

# <<<<<<< HEAD

# def show(request, id):
#     lessons = get_object_or_404(Order, pk=id)
#     return render(request, 'lessons/show.html', {"lessons": lessons})

# def home(request):
#     return render(request, 'home.html')

# =======
# def show(request, id):
#     lessons = get_object_or_404(Order, pk=id)
#     return render(request, 'lessons/show.html', {"lessons": lessons})


def first(request):
    return render(request, 'first.html')

