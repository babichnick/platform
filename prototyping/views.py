from django.shortcuts import render

from .models import Tool, PrototypingTool, Publication

def index(request):

    context={}
    return render(request, 'index.html', context=context)

def prototyping(request):
    prototyping_tools = PrototypingTool.objects.filter(published=True)
    context = {'prototyping_tools': prototyping_tools}
    return render(request, 'prototyping.html', context = context)

def tool(request, abbr):
    tool = Tool.objects.filter(abbreviation=abbr)
    context = {'tool': tool }
    return render(request, 'tool.html', context = context)


def blog(request, page=1):
    publications = Publication.objects.all()
    context = {'publications': publications }
    return render(request, 'blog.html', context=context)
