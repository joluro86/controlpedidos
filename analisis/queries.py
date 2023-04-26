
from analisis.models import Acta_analisis

def analisis_acta():
    A04mayor= Acta_analisis.objects.filter(item_cont='A 04', cantidad__gt=2)
    print(len(A04mayor))
    for a in A04mayor:
        print(a)