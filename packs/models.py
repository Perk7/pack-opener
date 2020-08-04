from django.db import models
from datetime import datetime    
from decimal import Decimal
from django.conf import settings
from django.utils import timezone
from copy import deepcopy
from django.shortcuts import get_object_or_404

# Паки

class Pack(models.Model):

	name = models.CharField(max_length=16)
	prescript = models.TextField(max_length=105)
	cost = models.IntegerField()
	icon = models.ImageField(upload_to='packs', height_field=None, width_field=None, max_length=100)

	pubdate = models.DateTimeField(default=datetime.now())

	class Meta:
	    verbose_name = 'Пак'
	    verbose_name_plural = 'Паки'

# Карточки

class Card(models.Model):
	name = models.CharField(max_length=16)
	quicksell = models.IntegerField()
	image = models.ImageField(upload_to='cards', height_field=None, width_field=None, max_length=100)
	chance = models.IntegerField()

	pubdate = models.DateTimeField(default=datetime.now())

	class Meta:
	    verbose_name = 'Карточка'
	    verbose_name_plural = 'Карточки'