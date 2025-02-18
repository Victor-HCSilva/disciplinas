from django.shortcuts import render, redirect, get_object_or_404
from . import urlsNames as uname
from . import functions as fc
from . forms import *
from django.http import Http404
from .forms import AnaliseForm

def analise(request):
    context = {
        'INDEX':uname.INDEX ,
        'LIST':uname.LIST,    
        'EDIT':uname.EDIT,
        'DELETE':uname.DELETE,
        'GROUP':uname.GROUP,    
        "CH":uname.CH,
        }
    return render(request, f"{uname.PATH_CH}", context)

def add_ch(request):
    if request.method == "POST" and form.is_valid():
        form = AnaliseForm(request.POST)
        form.save()
        return redirect(uname.LIST)
    else:
        form = AnaliseForm()

    context = {
        'INDEX':uname.INDEX,
        'LIST':uname.LIST,    
        'EDIT':uname.EDIT,
        'DELETE':uname.DELETE,
        'GROUP':uname.GROUP,
        "CH":uname.CH,
        "form":form,
        }
    return render(request, f"{uname.PATH_ADICIONAR_CH}", context)


