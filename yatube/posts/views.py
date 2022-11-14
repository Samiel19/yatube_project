from django.shortcuts import render, HttpResponse



def group_posts(request, slug):
    return HttpResponse(f'Посты группы {slug}')

    # Create your views here.
def index(request):
    return HttpResponse('Главная страница')
