from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR,"TEMPLATES)'
)

def index(request):
    return render(request, "index.html")

def valorRef(request):
    return render (request, "sistemas/valoresRef.html")

def altaInterV(request):
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

def altaEnsayoV(request):
    if request.method == 'POST':
        if request.POST.get('clavePrueba'):
            i = altaEnsayos2()
            i.nombreSolicitante = request.POST.get('NombreSolicitante')
            i.areaSolicitante = request.POST.get('AreaSolicitante')
            i.fechaSolicitud = request.POST.get('FechaSolicitud')
            if request.POST.get('checkbox1'):
                i.intercambio = True
            else:
                i.intercambio = False
            if request.POST.get('checkbox2'):
                i.porCobrar = True
            else:
                i.porCobrar = False
            if request.POST.get('checkbox3'):
                i.pasteur = True
            else:
                i.pasteur = False
            if request.POST.get('checkbox4'):
                i.modulab = True
            else:
                i.modulab = False

            # i.opciones = request.POST.get('checkbox1', 'checkbox2','checkbox3', 'checkbox4')
            i.proyecto = request.POST.get('Proyecto')
            i.claveEnsayo = request.POST.get('clavePrueba')
            i.nombreEnsayo = request.POST.get('NombreEnsayo')
            # i.ensayooperfil = request.POST.get('Type')
            if request.POST.get('radio1'):
                i.ensayooperfil = True
            else:
                i.ensayooperfil = False
            i.laboratorio = request.POST.get('select1')
            i.tipoMuestra = request.POST.get('select2')
            i.condiciones = request.POST.get('text3')
            i.motivosRechazo = request.POST.get('text4')
            i.tiempoEntrega = request.POST.get('text5')
            i.precio = request.POST.get('text6')
            i.save()
            return render(request, "index.html")
        
    else:
        return render(request, "sistemas/altaEnsayos.html")