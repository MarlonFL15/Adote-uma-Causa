from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app_adote_uma_causa/home.html')

def projects(request):
    return render(request, 'app_adote_uma_causa/projects.html')

def contact(request):
    return render(request, 'app_adote_uma_causa/contact.html')

def about(request):
    return render(request, 'app_adote_uma_causa/about.html')

def base(request):
    return render(request, 'app_adote_uma_causa/base.html')