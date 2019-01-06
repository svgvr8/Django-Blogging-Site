from django.shortcuts import render, redirect

from .forms import ContactForm
# Create your views here.
def contact_view(request):
	contact_form = ContactForm(request.POST or None)
	if contact_form.is_valid():
		contact_form.save()
		#return redirect('/contact/')
		return redirect('contact-view')
	context = {
	    "form" : contact_form
	}
	return render(request,"contact/form.html", context)