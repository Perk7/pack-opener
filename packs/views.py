from django.shortcuts import render

def base(request):
	return render(request, 'base.html')

def index(request):
	return render(request, 'index.html')

def collection(request):
	return render(request, 'collection.html')

def donate(request):
	return render(request, 'donate.html')

def reset(request):
	return render(request, 'reset.html')
