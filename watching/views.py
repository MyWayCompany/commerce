from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

from auctions.models import Listing

# Create your views here.
def index(request):
    return render(request, "watching/index.html", {
        "listings": request.user.watch_listing.all()
    })

def watching_listing(request, listing_id):
    try:
        request.user.watch_listing.add(Listing.objects.get(id=listing_id))
        return HttpResponseRedirect(reverse("index"))
    except Exception as e:
        return render(request, "auctions/", {
            "error_watching": "Не удалось добавить объявление  вотслеживаемое"
        })