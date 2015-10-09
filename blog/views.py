from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Postear

def listar_publicaciones(request):
    publicaciones = Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_publicaciones.html',{'publicaciones':publicaciones})

def detalle_publicaciones (request, pk):
    publicaciones = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/detalle_publicaciones.html',{'publicaciones':publicaciones})
