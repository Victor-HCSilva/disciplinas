from django.shortcuts import render, redirect, get_object_or_404
from . import urlsNames as uname
from . import functions as fc
from . forms import *
from django.http import Http404

def grupos(grupo):
    return Disciplina.objects.filter(grupo=grupo)

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
        'INDEX':uname.INDEX ,
        'LIST':uname.LIST,    
        'EDIT':uname.EDIT,
        'DELETE':uname.DELETE,
        'GROUP':uname.GROUP,
        'form_disciplina': form_disciplina,
    }

    return render(request, uname.PATH_INDEX, context=context)

def list(request):#GET
    if (request.method == "GET"):
        objects = Disciplina.objects.all()
        context = {
            'INDEX':uname.INDEX ,
            'LIST':uname.LIST,    
            'EDIT':uname.EDIT,
            'DELETE':uname.DELETE,
            'GROUP':uname.GROUP,
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
            'INDEX':uname.INDEX ,
            'LIST':uname.LIST,    
            'EDIT':uname.EDIT,
            'DELETE':uname.DELETE,
            'GROUP':uname.GROUP,
            'form':form,
            'disciplina':disciplina,
        }
        return render(request,uname.PATH_EDIT, context)
    
def delete(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)

    if request.method == 'POST':  # Use POST para a exclusão
        disciplina.delete()
        return redirect(uname.LIST)  # Redireciona para a lista de disciplinas
    context = {
        'disciplina': disciplina,
        'INDEX':uname.INDEX ,
        'LIST':uname.LIST,    
        'EDIT':uname.EDIT,
        'DELETE':uname.DELETE,
        'GROUP':uname.GROUP,
        
        }

    # Se for GET, exibe uma página de confirmação
    return render(request, uname.PATH_DELETE,context )

def group(request):#GET
    if (request.method == "GET"):
        group1 = grupos(1)
        group2 = grupos(2)
        group3 = grupos(3)
        disciplinas = Disciplina.objects.all()
        
        context = {
            'disciplinas':disciplinas,
            'INDEX':uname.INDEX ,
            'LIST':uname.LIST,    
            'EDIT':uname.EDIT,
            'DELETE':uname.DELETE,
            'GROUP':uname.GROUP,
            'grupo1':group1,
            'grupo2':group2,
            'grupo3':group3,
        }
        return render(request,uname.PATH_GROUP, context)
    else:
        raise Http404("Erro Tipo de requisição inválida")

def pag(request):#GET
    context = {
        'INDEX':uname.INDEX ,
        'LIST':uname.LIST,    
        'EDIT':uname.EDIT,
        'DELETE':uname.DELETE,
        'GROUP':uname.GROUP,
        }
    return render(request,uname.PATH_BASE, context)
    
    