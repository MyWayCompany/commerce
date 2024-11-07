from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="watching"),
    path("<int:listing_id>", views.watching_listing, name='watching_list')
]