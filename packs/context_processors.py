from .models import Collection, Card

def pack(request):
	collection = len(Collection(request))
	all_cards = Card.objects.all().count()
	money = request.session["money"]
	return {'all_collection': collection,
    		'all_cards' : all_cards,
    		'all_money' : money,
    		}