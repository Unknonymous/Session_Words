# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import datetime


# Create your views here.

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'log' not in request.session:
        request.session['log'] = []
    return render(request, 'sesswords/index.html')

def process(request):
    #set vars to build session item
    if 'variant' not in request.POST:
        return HttpResponse ('color selection is required')
    else:
        newWord = request.POST['newWord']
        color = request.POST['variant']
        time = datetime.datetime.now().strftime("%I:%M:%S%p")
        date = datetime.datetime.now().strftime("%B %d, %Y")
        if 'size' in request.POST:
            size = 'big'
        else:
            size = 'normal'
    
    request.session['log'].append({'word':newWord, 'color':color, 'size':size, 'time':time, 'date':date})
    request.session['count'] += 1
    return redirect ('/')

def clear(request):
    request.session.flush()
    return redirect ('/')
