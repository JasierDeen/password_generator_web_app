from django.shortcuts import render
import string
import secrets


def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    length = int(request.GET.get("length", 12))
    combination = string.ascii_lowercase
    if request.GET.get("special"):
        combination += string.punctuation

    if request.GET.get("uppercase"):
        combination += string.ascii_uppercase

    if request.GET.get("numbers"):
        combination += string.digits

    combination_length = len(combination)
    new_password = ''
    
    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]
    
    return render(request, 'generator/password.html' , {'password': new_password})

def about(request):
    return render(request, 'generator/about.html')