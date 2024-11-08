from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime


from auctions.models import Category, Listing, Comment
# Create your views here.
def index(request):
    return render(request, "listings/index.html")

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        start_price = request.POST["start_price"]
        date_time = datetime.datetime.now()  
        user = request.user
        category = Category.objects.get(id=request.POST["category"])
        preview = request.FILES["preview"]       
        try:
            Listing.objects.create(title=title, description = description, start_price = start_price, dateTime_creation = date_time, user = user, category = category, preview = preview)
            return  HttpResponseRedirect(reverse("index"))
        except Exception as e:
            return render(request, "listings/create.html", {
                "message": F"Не удалось создать объявлениеб ошибка: {e}",
                "categories": Category.objects.all()
            })
    else:
        return render(request, "listings/create.html", {
            "categories": Category.objects.all()
        })
    
def detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, "listings/detail.html", {
        "listing": listing,
        "comments": listing.comment.all(),
        "count_comments": listing.comment.count()
    })


def create_comment(request, listing_id):
    if request.method == "POST" and request.POST["text"]:
        try:
            text = request.POST["text"]
            listing  = Listing.objects.get(id=listing_id)
            comment = Comment.objects.create(text=text, dateTime_creation = datetime.datetime.now(), user = request.user)
            listing.comment.add(comment)
            return render(request, "listings/detail.html", {
                "listing": listing,
                "comments": listing.comment.all(),
                "count_comments": listing.comment.count()
            })
        except Exception as e:
            return render(request, "listings/detail.html", {
                "listing": Listing.objects.get(id=listing_id),
                "message": F"Не удалось создать комментарий, {e}"
            })
    else:
        return render(request, "listings/detail.html", {
            "listing": Listing.objects.get(id=listing_id),
            "comments": Listing.objects.get(id=listing_id).comment.all(),
            "count_comments": Listing.objects.get(id=listing_id).comment.count()
        })