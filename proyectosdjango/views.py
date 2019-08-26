from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Renderiza la plantilla HTML index.html
    return render(
        request,
        'index.html',
    )

