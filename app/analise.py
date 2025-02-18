from django.shortcuts import render, redirect, get_object_or_404
from . import urlsNames as uname
from . import functions as fc
from . forms import *
from django.http import Http404
from .forms import AnaliseForm
import matplotlib.pyplot as plt
from .models import Analise

def analise(request):
    ch = Analise.objects.all()
    context = {
        'INDEX':uname.INDEX ,
        'LIST':uname.LIST,
        'EDIT':uname.EDIT,
        'DELETE':uname.DELETE,
        'GROUP':uname.GROUP,
        "CH":uname.CH,
        "ADICIONAR_CH":uname.ADICIONAR_CH,
        "ch":ch,
        }
    return render(request, f"{uname.PATH_CH}", context)

def add_ch(request):
    if request.method == "POST":
        form = AnaliseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(uname.LIST)
    else:
        form = AnaliseForm()
        grafico = plt.plot([1,2,3,4],[2,3,4,5])
        #plt.show()

    context = {
        'INDEX':uname.INDEX,
        'LIST':uname.LIST,
        'EDIT':uname.EDIT,
        'DELETE':uname.DELETE,
        'GROUP':uname.GROUP,
        "CH":uname.CH,
        "ADICIONAR_CH":uname.ADICIONAR_CH,
        "form":form,
        }
    return render(request, f"{uname.PATH_ADICIONAR_CH}", context)

def atualizar(request):
    return render()
