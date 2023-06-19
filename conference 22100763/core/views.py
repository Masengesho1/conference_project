from django.http import HttpResponse
from django.shortcuts import render


def shield_view(request):
    data = ['django', 'laravel', 'asp.net core', 'express']
    return render(request, 'shield.html', {'data': data})


def about_view(request):
    return HttpResponse("<h1>About Page</h1><br><a href='/'>Go back to home</a>")


def checking_stuff(request, number):
    # DB query
    #
    # number = ''
    # if id < 5:
    #     number = 'xzy'
    return render(request, 'checking.html', {'number': number})