from django.shortcuts import render


def index(request):
    context = {}
    return render(request, template_name='temp/../../templates/home.html', context=context)
