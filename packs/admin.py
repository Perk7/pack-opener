from django.contrib import admin

from .models import Card, Pack, ChanceForPacks

admin.site.register(Card)
admin.site.register(Pack)
admin.site.register(ChanceForPacks)