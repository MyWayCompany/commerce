from django.shortcuts import render

from auctions.models import Category
# Create your views here.
def index(request):
    return render(request, "listings/index.html")

def create(request):
    return render(request, "listings/create.html", {
        "categories": Category.objects.all()
    })