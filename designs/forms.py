from django import forms
from .models import Design, DesignCategory

class DesignForm(forms.ModelForm):

    class Meta:
        model = Design
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        designcategories = DesignCategory.objects.all()
        friendly_names = [(d.id, d.get_friendly_name()) for d in designcategories]

        self.fields['designcategory'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'