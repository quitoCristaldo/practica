from django.shortcuts import render

def lista_prod(request):
    return render(request=request,
     template_name='productos/lista.html',
     context= {})