from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def capsule_list(request):
    capsule = Capsule.objects.filter(available = True)
    return render(request, 'capsule/list.html', {'capsule': capsule,})

def capsule_detail(request,slug):
    capsule = Capsule.objects.filter(slug=slug)
    return render(request, 'capsule/detail.html', {'capsule': capsule, 'slug': slug,})

