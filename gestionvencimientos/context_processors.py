
from perseovsfenix.models import NumeroActa

def numero_acta(request):
    numero_acta_actual = NumeroActa.objects.first()
    return {'numero_acta_actual': numero_acta_actual}