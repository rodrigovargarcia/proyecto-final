from django import forms
from ejemplo.models import Familiar
from ejemplo.models import Mascota

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=10)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['raza', 'edad']