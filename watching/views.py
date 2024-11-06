from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "watching/index.html", {
        "watching_listings": request.user.watch_listing.all()
    })