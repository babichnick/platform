from django.shortcuts import render

from .models import PrototypingTool

def index(request):

    context={}
    return render(request, 'index.html', context=context)

def prototyping(request):
    prototyping_tools = PrototypingTool.objects.filter(published=True)
    context = {'prototyping_tools': prototyping_tools}
    return render(request, 'prototyping.html', context = context)

