from django.db.models import Q
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from .models import Post

def post_list_view(request):
	qs = Post.objects.all()
	Suggested = Post.objects.all().order_by('?')
	context = {
	   'object_list' : qs,
	   'random_list' : Suggested,
	}
	return render(request, "posts/list.html", context)


def post_detail_view(request, id=None):

	#try:
	#    obj = Post.objects.get(id=id)
	#except:
	#	raise Http404
	obj = get_object_or_404(Post, id=id)
	context = {
	   'object' : obj
	}
	return render(request, "posts/detail.html", context)

def post_search_view(request):

	request_params = request.GET
	query = request_params.get("q")
	qs = Post.objects.none()
	if query:
	    qs = Post.objects.filter(
	    	   Q(title__icontains=query) |
	           Q(content__icontains=query)
	        )
	context = {
	   'object_list' : qs
	}
	return render(request, "posts/list.html", context)