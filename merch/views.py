from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,"home.html", {})

def merch(request):
	mydict = {"mytitle" : "About Us",
	"headtitle" : "About Us" }
	return render(request,"merch.html", mydict )