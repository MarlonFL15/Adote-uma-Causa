from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from .request import make_request
from googletrans import Translator


themes = {
    'hunger':'Comida saudável',
    'water': 'Água potável',
    'health': 'Assistência médica',
    'housing': 'Acesso à moradia',
    'edu': 'Educação',
    'children': 'Proteção infantil',
    'animals': 'Bem-estar animal',
    'climate': 'Ações climáticas',
    'gender': 'Igualdade de gênero',
    'rights': 'Justiça e direitos humanos',
    'lgbt': 'Direitos LGBTQIA+',
    'justice': 'Igualdade Racial'
}

# Create your views here.

def home(request):
    url = 'https://api.globalgiving.org/api/public/projectservice/featured/projects'
    json = make_request(url)
    projects = []
    translator = Translator()
    for j in json['projects']['project']:
        projects.append({
            'title': j['title'],
            'id': j['id'],
            'summary': j['summary'],
            'funding': j['funding'],
            'goal': j['goal'],
            'percent': float(j['funding']) / float(j['goal']) * 100,
            'image_link': j['image']['imagelink'][3]['url']
        })
    return render(request, 'app_adote_uma_causa/home.html', {'projects':projects})

def projects(request, theme=None):
    projects = []
    theme = request.GET.get('theme','')
    translator = Translator()
    if theme != 'null' and theme:
        url = 'https://api.globalgiving.org/api/public/projectservice/themes/' + theme + '/projects/active'
        json = make_request(url)
        for j in json['projects']['project']:
            projects.append({
                'title': j['title'],
                'id': j['id'],
                'summary': j['summary'],
                'funding': j['funding'],
                'goal': j['goal'],
                'percent': float(j['funding']) / float(j['goal']) * 100,
                'image_link': j['image']['imagelink'][5]['url']
            })

        return render(request, 'app_adote_uma_causa/projects.html', {'themes': themes, 'current_theme':theme,
                                                                    'projects':projects})
    else:
        return render(request, 'app_adote_uma_causa/projects.html', {'themes': themes})

def about(request):
    return render(request, 'app_adote_uma_causa/about.html')

async def details(request, id):
    url = 'https://api.globalgiving.org/api/public/projectservice/projects/'+id
    json = make_request(url)['project']
    translator = Translator()
    project = {
        'title': json['title'],
        'summary': json['summary'],
        'activities': json['activities'],
        'need': json['need'],
        'image': json['image']['imagelink'][5]['url'],
        'funding': json['funding'],
        'goal': json['goal'],
        'percent': float(json['funding']) / float(json['goal']) * 100,
    }

    return render(request, 'app_adote_uma_causa/single.html', {'project': project})
