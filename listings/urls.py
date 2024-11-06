from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="listings"),
    path("create", views.create, name="create_listing"),
    path("<int:listing_id>", views.detail, name="detail"),
    path("<int:listing_id>", views.watching_listing, name='watching')
]

# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)