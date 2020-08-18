from django.db import models
from datetime import datetime    
from decimal import Decimal
from django.conf import settings
from django.utils import timezone
from copy import deepcopy
from django.shortcuts import get_object_or_404

import random

# Карточки

class Card(models.Model):
	name = models.CharField(max_length=16)
	quicksell = models.IntegerField()
	image = models.CharField(max_length=500)

	raiting = models.IntegerField()
	typecard = models.CharField(max_length=10)

	pubdate = models.DateTimeField(default=timezone.now)

	class Meta:
	    verbose_name = 'Карточка'
	    verbose_name_plural = 'Карточки'

# Паки

class ChanceForPacks(models.Model):
	two = models.CharField(max_length=30)
	five = models.CharField(max_length=30)
	twelve = models.CharField(max_length=30)
	twenty_eight = models.CharField(max_length=30)
	fourty = models.CharField(max_length=30)
	fifty = models.CharField(max_length=30)
	sixty_four = models.CharField(max_length=30)
	eighty_two = models.CharField(max_length=30)
	hundred = models.CharField(max_length=30)

	class Meta:
	    verbose_name = 'Шанс пака'
	    verbose_name_plural = 'Шансы паков'

class Pack(models.Model):
	chance = models.OneToOneField(ChanceForPacks, on_delete = models.CASCADE)
	name = models.CharField(max_length=16)
	prescript = models.TextField(max_length=105)
	cost = models.IntegerField()
	icon = models.CharField(max_length=500)
	#icon = models.ImageField(upload_to='packs', height_field=None, width_field=None, max_length=100)

	pubdate = models.DateTimeField(default=timezone.now)

	class Meta:
	    verbose_name = 'Пак'
	    verbose_name_plural = 'Паки'

	def internal_open(self, raiting, splited):
		if splited[1] != "all":
			typeof = splited[1].split(' ')
			variant = Card.objects.filter(typecard__in=typeof).filter(raiting__in=raiting)
			return random.choice(variant)
		else:
			variant = Card.objects.filter(raiting__in=raiting)
			return random.choice(variant)

	def open(self):
		chances = [(self.chance.two.split(','), 2),
				   (self.chance.five.split(','), 5),
				   (self.chance.twelve.split(','), 12),
				   (self.chance.twenty_eight.split(','), 28),
				   (self.chance.fourty.split(','), 40),
				   (self.chance.fifty.split(','), 50),
				   (self.chance.sixty_four.split(','), 64),
				   (self.chance.eighty_two.split(','), 82),
				   (self.chance.hundred.split(','), 100)]
		result = random.randint(1,100)
		pre_raiting = 100

		for splited, num in chances: 
			if int(splited[0]) != pre_raiting:
				raiting = [i for i in range(int(splited[0]),pre_raiting)]
				pre_raiting = int(splited[0])
			if result <= num:
				finish = self.internal_open(raiting, splited)
				return finish

# Коллекция

class Collection(object):
	def __init__(self, request):
		self.session = deepcopy(request.session)
		self.last_session = request.session
		if 'money' not in request.session.keys():
			request.session["money"] = 0
		cards = [card.name for card in Card.objects.all()]
		for i in list(self.session.keys()):
			if i not in cards:
				del self.session[i]

	def add(self, card):
		if card.name not in self.session.keys():
			self.session[card.name] = {
										'img' : card.image,
										'raiting' : card.raiting,										
										}	
			self.last_session[card.name] = {
										'img' : card.image,
										'raiting' : card.raiting,										
										}				
		self.save()

	def save(self):
		# Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
		self.session.modified = True

	def remove(self, card):
		name = str(card.name)
		if name in self.session.keys():
			del self.session[name]
			del self.last_session[name]		
			self.save()

	def __iter__(self):
		for item in self.session.values():
			yield item

	def __len__(self):
		return len(list(self.session.keys()))

	def clear(self):
		# удаление корзины из сессии
		it = deepcopy(self.session)
		for i in it.keys():
			self.remove(Card.objects.get(name = i))