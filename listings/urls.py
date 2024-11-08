from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="listings"),
    path("create", views.create, name="create_listing"),
    path("listing/<int:listing_id>", views.detail, name="detail"),
    path("listing/<int:listing_id>/comment", views.create_comment, name="comment"),
]

# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)