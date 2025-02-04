from django.shortcuts import render, redirect, get_object_or_404
from . import urlsNames as uname
from . import functions as fc
from . forms import *
from django.http import Http404

def index(request):#POST
    if request.method == 'POST':    
        form_disciplina = DisciplinaForm(request.POST)  
        form_pro = NomeProfessorForm(request.POST)
        form_nome_disciplina = NomeDisciplinaForm(request.POST)
        form_nome_curso = NomeCursoForm(request.POST)
        form_ch = CargaHorariaForm(request.POST)
        form_codigo = CodigoForm(request.POST)

        if (form_disciplina.is_valid()):
            form_disciplina.save() 
            return redirect(uname.LIST) 
        
        elif (form_pro.is_valid()):
            form_pro.save() 
            return redirect(uname.LIST) 
        
        elif form_nome_disciplina.is_valid():
            form_nome_disciplina.save() 
            return redirect(uname.LIST) 
        
        elif form_nome_curso.is_valid():
            form_nome_curso.save() 
            return redirect(uname.LIST) 
        
        elif form_ch.is_valid():
            form_ch.save() 
            return redirect(uname.LIST) 
        
        elif form_codigo.is_valid():
            form_codigo.save() 
            return redirect(uname.LIST) 
        
        
    else:
        form_disciplina = DisciplinaForm()  
        form_pro = NomeProfessorForm()
        form_nome_disciplina = NomeDisciplinaForm()
        form_nome_curso = NomeCursoForm()
        form_ch = CargaHorariaForm()
        form_codigo = CodigoForm()

    context = {
        'INDEX':uname.INDEX ,
        'form_disciplina': form_disciplina,
        'form_pro': form_pro,
        'form_nome_disciplina': form_nome_disciplina,
        'form_nome_curso': form_nome_curso,
        'form_ch': form_ch,
        'form_codigo': form_codigo,
    }
    
    return render(request,uname.PATH_INDEX,context=context)

def list(request):#GET
    if (request.method == "GET"):
        context = {
            'INDEX':uname.INDEX ,
        }
        return render(request,uname.PATH_LIST, context)
    else:
        raise Http404("Erro tipo de requisição inválida")