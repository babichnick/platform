from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from .models import Tool, PrototypingTool, Publication

def index(request):
    publications_list = Publication.objects.order_by('-pub_date')
    

    paginator = Paginator(publications_list, 14) # Show 14 latest publications

    page = request.GET.get('page')
    publications = paginator.get_page(page)

    
    if page:
        context = {'publications': publications }
        return render(request, 'index_paginated.html', context=context)
    else:
        head_post = publications[0]
        first_six_posts = publications[1:7]
        second_six_posts = publications[7:13]
        tail_post = publications[13]
        context = {
                'headpost': head_post,
                'firstsixposts': first_six_posts,
                'secondsixposts': second_six_posts,
                'tailpost': tail_post,
                }
        return render(request, 'index.html', context=context)

def prototyping(request):
    prototyping_tools = PrototypingTool.objects.filter(published=True)
    context = {'prototyping_tools': prototyping_tools}
    return render(request, 'prototyping.html', context = context)

def tool(request, abbr):
    tool = Tool.objects.get(abbreviation=abbr)
    context = {'tool': tool }
    return render(request, 'tool.html', context = context)


def blog(request, page=1):
    publications = Publication.objects.all()
    context = {'publications': publications }
    return render(request, 'blog.html', context=context)
