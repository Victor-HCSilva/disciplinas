from django.shortcuts import render, redirect, get_object_or_404
from . import urlsNames as uname
from . import functions as fc
from . forms import *
from django.http import Http404

def index(request):#POST
    form_disciplina = None  # Inicializa como None para verificar se foi processado
    
    if request.method == 'POST':
        form_disciplina = DisciplinaForm(request.POST)
        if form_disciplina.is_valid():
            form_disciplina.save()
            return redirect(uname.LIST)
        else:
            print("Erro no Form Disciplina:", form_disciplina.errors) #Debugging
    else:
        form_disciplina = DisciplinaForm()
    context = {
        'INDEX': uname.INDEX,
        'form_disciplina': form_disciplina,
    }

    return render(request, uname.PATH_INDEX, context=context)

def list(request):#GET
    if (request.method == "GET"):
        objects = Disciplina.objects.all()
        context = {
            'INDEX':uname.INDEX ,
            'disciplinas':objects,
        }
        return render(request,uname.PATH_LIST, context)
    else:
        raise Http404("Erro Tipo de requisição inválida")
    
def edit(request, id):#GET
    disciplina = get_object_or_404(Disciplina, id=id)

    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)  
        if form.is_valid():
            form.save()
            return redirect(uname.LIST)
    else: 
        form = DisciplinaForm(instance=disciplina) 
        context = {
            'form':form,
            'disciplina':disciplina,
        }
        return render(request,uname.PATH_EDITE, context)
    
def delete(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)

    if request.method == 'POST':  # Use POST para a exclusão
        disciplina.delete()
        return redirect(uname.LIST)  # Redireciona para a lista de disciplinas

    # Se for GET, exibe uma página de confirmação
    return render(request, uname.PATH_DELETE, {'disciplina': disciplina})