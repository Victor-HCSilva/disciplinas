from django import forms
from .models import (
    Disciplina,
    Analise,
)


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

class AnaliseForm(forms.ModelForm):
    class Meta:
        model = Analise
        fields = "__all__"
