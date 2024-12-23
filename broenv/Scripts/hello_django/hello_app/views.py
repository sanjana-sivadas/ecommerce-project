from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def print_hello(request):
    movie_data={
        'movies':
        [{
        'title':'godfather',
        'year':1990,
        'summary':'story of an underworld king',
        'success':False
    },
    {
        'title':'hridayam',
        'year':2021,
        'success':False
    },
    {
        'title':'goatlife',
        'year':2024,
        'summary':'story of a man',
        'success':False
    }
    ]}
    return render(request,'hello.html',movie_data)