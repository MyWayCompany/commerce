from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="listings"),
    path("create", views.create, name="create_listing")
]

