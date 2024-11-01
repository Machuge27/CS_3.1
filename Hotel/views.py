# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Passphrase
from django.http import JsonResponse

import json

def home(request):
    if request.method=='POST':
        data=json.loads(request.body)   
        instance=Passphrase.objects.create(code=data['data']['Passphrase'])
        return JsonResponse({'success':True})
    return render(request, 'hotel/main.html')

