from email import message
from django.shortcuts import render
from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    data_watchlist = WatchList.objects.all()

    movie_watched = 0
    movie_watched_no = 0
    message = ""
    for movie in data_watchlist:
        if (movie.watched == True):
            movie_watched+=1
        else:
            movie_watched_no+=1
    
    if(movie_watched>movie_watched_no):
        message = "Selamat, kamu sudah banyak menonton!"
    else: 
        message = "Wah, kamu masih sedikit menonton!"

    context = {
        'watchlist': data_watchlist,
        'nama': 'Griselda Neysa Sadiya',
        'npm' : '2106751392',
        'message' : message
    }
    return render(request, "mywatchlist.html", context)

def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
