from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem
def show_katalog(request):
    data_item_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog' : data_item_katalog,
        'nama' : 'Reza Taufiq Yahya',
        'NPM' : '2106654183',  
    }
    return render(request, "katalog.html", context)
# TODO: Create your views here.
