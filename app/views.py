from django.shortcuts import render, redirect, get_object_or_404
from . import urlsNames as uname
from . import functions as fc
from . forms import *
from django.http import Http404

context = {
        'INDEX':uname.INDEX ,
        'LIST':uname.LIST,
        'EDIT':uname.EDIT,
        'DELETE':uname.DELETE,
        'GROUP':uname.GROUP,
        "CH":uname.CH,
        "ADICIONAR_CH":uname.ADICIONAR_CH,
        "ATUALIZAR_CH":uname.ATUALIZAR_CH,
        }

#metodo de função
def grupos(grupo):
    return Disciplina.objects.filter(grupo=grupo)

def cursando():
    return Disciplina.objects.filter(cursando=True)

def horas(model):
    soma = 0
    for h in model:
        if h.cursando:
            h.carga_horaria = h.carga_horaria.replace("h","")
            soma += int(h.carga_horaria)
    return soma

def index(request):#POST
    form_disciplina = DisciplinaForm()  # Inicializa como None para verificar se foi processado

    if request.method == 'POST':
        form_disciplina = DisciplinaForm(request.POST)
        if form_disciplina.is_valid():
            form_disciplina.save()
            return redirect(uname.LIST)
        else:
            print("Erro no Form Disciplina:", form_disciplina.errors) #Debugging

    elif request.GET == "GET":
        form_disciplina = DisciplinaForm()

    context["form_disciplina"] = form_disciplina
    return render(request, uname.PATH_INDEX, context=context)

def list(request):#GET
    if (request.method == "GET"):
        objects = Disciplina.objects.all()
        context["disciplinas"] = objects
        return render(request,uname.PATH_LIST, context)
    else:
        raise Http404("Tipo de requisição inválida")

def edit(request, id):#GET
    disciplina = get_object_or_404(Disciplina, id=id)

    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect(uname.LIST)
    else:
        form = DisciplinaForm(instance=disciplina)
        context["form"] = form
        context["disciplina"] = disciplina
        return render(request,uname.PATH_EDIT, context)

def delete(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)

    if request.method == 'POST':  # Use POST para a exclusão
        disciplina.delete()
        return redirect(uname.LIST)  # Redireciona para a lista de disciplinas

   # Se for GET, exibe uma página de confirmação
    return render(request, uname.PATH_DELETE,context )

def group(request):#GET
    if (request.method == "GET"):
        group1 = grupos(1)
        group2 = grupos(2)
        group3 = grupos(3)
        disciplinas = Disciplina.objects.all()
        context["disciplinas"] = disciplinas
        context["grupo1"] = group1
        context["grupo2"] = group2
        context["grupo3"] = group3
        return render(request,uname.PATH_GROUP, context)
    else:
        raise Http404("Tipo de requisição inválida")

def pag(request):#GET
    return render(request,uname.PATH_BASE, context)

def main(request):#GET
    if (request.method == "GET"):
        objects = Disciplina.objects.all()
        materias_atuais = cursando() 
        context["disciplinas"] = materias_atuais
        context["horas"] = horas(objects)
        return render(request,uname.PATH_LIST, context)
 
