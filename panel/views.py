from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import altaInter

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR,"TEMPLATES)'
)

def index(request):
    return render(request, "index.html")

def valoresRef(request):
    return render (request, "sistemas/valoresRef.html")

def altaInterfAZ(request):
    if request.method == 'POST':
        if request.POST.get('ensayo') and request.POST.get('CodHost') and request.POST.get('instrumento'):
            i = altaInter()
            i.ensayo = request.POST.get('ensayo')
            i.host = request.POST.get('CodHost')
            i.analizador = request.POST.get('instrumento')
            i.save()
            return render(request, "index.html")

    else:
        return render(request, "sistemas/altaInter.html")

def altaEnsayos(request):
    return render(request, "sistemas/altaEnsayos.html")