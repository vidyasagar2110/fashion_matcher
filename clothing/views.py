from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def male_clothing(request):
    return render(request, 'male_clothing.html')

def female_clothing(request):
    return render(request, 'female_clothing.html')

def match_clothing(request):
    return render(request, 'match_clothing.html')
