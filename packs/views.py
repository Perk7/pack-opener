from django.shortcuts import render, redirect
from packs.models import Card, Pack, Collection
from django.shortcuts import get_object_or_404

def base(request):
	return render(request, 'base.html')

def index(request):
	collection = Collection(request)
	pack = get_object_or_404(Pack, name="DEFAULT PACK")
	card = pack.open()
	info = card.name if card.name not in collection.session.keys() else "QuickSell of card" 
	return render(request, 'index.html', {'card' : card,
										  'pack' : pack,
										  'info' : info})

def collection(request):
	collection = Collection(request)
	collection.update()
	collection = Collection(request)

	collection = list(collection.session.values())
	collection_sorted = sorted(collection, key=lambda card: card['raiting'], reverse=True)

	progress = len(collection)*100/Card.objects.all().count() if len(collection) else 0
	return render(request, 'collection.html', {'collection' : collection_sorted,
											   'progress' : int(progress)})
 
def shop(request):
	packs = Pack.objects.exclude(name='DEFAULT PACK').order_by('cost')
	if packs:
		return render(request, 'shop.html', {'packs' : packs,})
	return render(request, 'shop.html', {'packs' : {}})

def donate(request):
	return render(request, 'donate.html')

def reset(request):
	return render(request, 'reset.html')

def open_pack(request):
	if request.method == 'POST':
		pack_name = request.POST['pack']
		pack = get_object_or_404(Pack, name=pack_name)
		request.session["money"] -= pack.cost
		card = pack.open()
		collection = Collection(request)
		info = card.name if card.name not in collection.session.keys() else "QuickSell of card" 
		return render(request, 'index.html', {'card' : card,
										 	  'pack' : pack,
										  	  'info' : info})

def save_card(request):
	collection = Collection(request)
	if request.method == 'POST':
		card_name = request.POST['card']
		card = Card.objects.get(name = card_name)
		if card_name in collection.session.keys():
			request.session["money"] += card.quicksell
		if card_name not in collection.session.keys():
			collection.add(card)
		return redirect('/')

def collection_clear(request):
    collection = Collection(request)
    collection.clear()
    request.session["money"] = 0
    return redirect('/collection')

def pay_donate(request):
	return redirect('https://my.qiwi.com/Denys-PMkfk6zW-Z')