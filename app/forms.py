from django import forms
from .models import (
    Disciplina, Professor,
    Curso, NomeDisciplina,Codigo,
    CargaHoraria)


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = [
            'nome',
            'codigo',
            'descricao',
            'carga_horaria',
            'dia_da_semana',
            'professor',
            'curso',
            'grupo',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['professor'].queryset = Professor.objects.all()
        self.fields['curso'].queryset = Curso.objects.all()
        self.fields['nome'].queryset = NomeDisciplina.objects.all()

class NomeDisciplinaForm(forms.ModelForm):
    class Meta:
        model = NomeDisciplina
        fields = ['nome']
         
class NomeProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome']
         
class NomeCursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome']
         
class CargaHorariaForm(forms.ModelForm):
    class Meta:
        model = CargaHoraria
        fields = ['carga_horaria']

         
class CodigoForm(forms.ModelForm):
    class Meta:
        model = Codigo
        fields = ['codigo']

         
