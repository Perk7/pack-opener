from django.urls import path
from packs import views
from django.conf.urls.static import static

app_name="packs"
urlpatterns = [
    path('base', views.base),

    path('', views.index),
    path('collection', views.collection),
    path('shop', views.shop),
    path('donate', views.donate),
    path('reset', views.reset),

    path('open_pack', views.open_pack),
    path('save_card', views.save_card),
    path('collection_clear', views.collection_clear),
]