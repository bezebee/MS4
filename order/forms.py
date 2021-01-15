from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Email address'}))
    sketch_name= forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Sketch Name'}))
    sketch_sku = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Sketch SKU'}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Description'}))
    special_requests = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Special Requests'}))


# added 'form-control' for responsiveness

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'sketch_name', 'sketch_sku', 'description', 'special_requests')

