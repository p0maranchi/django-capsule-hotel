from django.shortcuts import render
from .models import *

# Create your views here.
def capsuleList(request):
    capsule = Capsule.objects.filter(available = True)
    return render(request, 'capsule/list.html', {'capsule': capsule,})

def capsuleDetail(request,slug):
    capsule = Capsule.objects.filter(slug=slug)
    return render(request, 'capsule/detail.html', {'capsule': capsule, 'slug': slug,})

