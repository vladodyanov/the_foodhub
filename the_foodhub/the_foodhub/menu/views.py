from django.shortcuts import render


def menu_builder(request):
    return render(request, 'vendor/menu_builder.html')
