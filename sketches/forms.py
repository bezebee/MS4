from django import forms
from .widgets import CustomClearableFileInput
from .models import Sketch, Sheet


class SketchForm(forms.ModelForm):

    class Meta:
        model = Sketch
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sheets = Sheet.objects.all()
        friendly_names = [(s.id, s.get_friendly_name()) for s in sheets]

        self.fields['sheet'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
