from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,"home.html", {})

def about(request):
	mydict = {"mytitle" : "About Us",
	"headtitle" : "About Us" }
	return render(request,"about.html", mydict )