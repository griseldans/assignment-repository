from django.shortcuts import render
from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers

def show_watchlist(request):
    data_watchlist = WatchList.objects.all()
    context = {
        'watchlist': data_watchlist,
        'nama': 'Griselda Neysa Sadiya',
        'npm' : '2106751392'
    }
    return render(request, "mywatchlist.html", context)

def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
