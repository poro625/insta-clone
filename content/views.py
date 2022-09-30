from django.shortcuts import render

def profile_view(request):
    return render(request, 'content/profile.html')

def home_view(request):
    return render(request, 'content/home.html')