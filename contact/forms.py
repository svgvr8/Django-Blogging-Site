from django import forms

from .models import Contact

BOOTSTRAP_CLASS = {'class':'form-control'}

class ContactForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs=BOOTSTRAP_CLASS))
	email = forms.CharField(widget=forms.EmailInput(attrs=BOOTSTRAP_CLASS))
	phone = forms.CharField(widget=forms.TextInput(attrs=BOOTSTRAP_CLASS), required=False)
	content = forms.CharField(widget=forms.Textarea(attrs=BOOTSTRAP_CLASS))
	class Meta:
		model = Contact
		fields = [
            'name',
            'email',
            'phone',
            'content',
		]