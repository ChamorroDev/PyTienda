from django.forms import (ModelForm,EmailField, EmailInput, CharField, PasswordInput,BooleanField,CheckboxInput,TextInput,NumberInput)
from autentificacion.models import Direccion

class DireccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = ('direccion', 'numeracion', 'ciudad')
        widgets = {
            'direccion' : TextInput( attrs = { 'class':'form-control' }),
            'numeracion' : NumberInput( attrs = { 'class':'form-control' }),
            'ciudad' : TextInput( attrs = { 'class':'form-control' })
        }