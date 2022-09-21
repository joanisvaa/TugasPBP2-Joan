from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_film_mywatchlist = MyWatchList.objects.all()
    context = {
    'list_film': data_film_mywatchlist,
    'nama': 'Joan Isva Shanti Andrea',
    'id': '2106707712'
}
    return render(request, "mywatchlist.html", context)

# def show_html(request):
#     data = MyWatchList.objects.all()
#     return HttpResponse(serializers.serialize("html", data), content_type="application/html")

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# def show_html_by_id(request, id):
#     data = MyWatchList.objects.filter(pk=id)
#     return HttpResponse(serializers.serialize("html", data), content_type="application/html")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
