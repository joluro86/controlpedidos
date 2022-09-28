from asyncio.windows_events import NULL
from datetime import date, datetime, timedelta
from email.policy import HTTP
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import holidays_co
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User, auth
import pandas as pd
from gestionvencimientos.views import cambiar_formato_fecha
from gestionvencimientos.models import *

def acrev(request): 
    aeneses = Ans.objects.filter(Actividad = "ACREV").filter(Q(Estado="PENDI") | Q(Concepto="406") | Q(Concepto="414")| Q(Concepto="495")| Q(Concepto="430"))
    aeneses = cambiar_formato_fecha(aeneses)
    return render(request, "acrev.html", {"aneses": aeneses} )

def inconsistencias(request):
    aeneses1 = Ans.objects.filter(Concepto='FSE') 
    aeneses2 = Ans.objects.filter(Concepto='INFSM')
    aenese=[]
    print(len(aeneses2))
    for a in aeneses1:
        aenese.append(a)
    for ae in aeneses2:
        aenese.append(ae)
    
    aeneses = cambiar_formato_fecha(aenese)
    return render(request, "inconsistencias.html", {"aneses": aeneses} )

def amrtr(request):   
    aeneses = Ans.objects.filter(Actividad = "AMRTR").filter(Q(Estado="PENDI") | Q(Concepto="406") | Q(Concepto="414")| Q(Concepto="495")| Q(Concepto="430"))
    aeneses = cambiar_formato_fecha(aeneses)

    return render(request, "amrtr.html", {"aneses": aeneses} )
   
def lega(request):
    
    aeneses = Ans.objects.filter(Q(Actividad="ALEGA") | Q(Actividad="ALEGN") | Q(Actividad="ALECA") |Q(Actividad="ACAMN") ).filter(Q(Estado="PENDI") | Q(Concepto="406") | Q(Concepto="414")| Q(Concepto="495")| Q(Concepto="430"))
    aeneses = cambiar_formato_fecha(aeneses)
    return render(request, "lega.html", {"aneses": aeneses} )

def programador(request):
    aeneses = Ans.objects.all()
    return render(request, "programador.html", {"aneses": aeneses} )

