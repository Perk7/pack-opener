from django.urls import path
from packs import views
from django.conf.urls.static import static

app_name="packs"
urlpatterns = [
    path('base', views.base),
    path('', views.index),
    path('collection', views.collection),
    path('donate', views.donate),
    path('reset', views.reset),
]