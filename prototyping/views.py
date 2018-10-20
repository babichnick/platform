from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404
from django.shortcuts import render

from .models import Tool, PrototypingTool, Publication

def index(request):
    publications_list = Publication.objects.all()#order_by('-pub_date')
    

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

def publications(request,slug):
    publication = Publication.objects.get(slug=slug)
    if publication.status == 1:
        raise Http404
    context = {'publication': publication}
    return render(request, 'publication.html', context = context)

def prototyping(request):
    prototyping_tools = PrototypingTool.objects.filter(published=True)
    context = {'prototyping_tools': prototyping_tools}
    return render(request, 'prototyping.html', context = context)

def alltools(request):
    prototyping_tools = PrototypingTool.objects.filter(published=True)
    context = {'prototyping_tools': prototyping_tools}
    return render(request, 'tools_all.html', context = context)

def prototypingtool(request, slug):
    tool = PrototypingTool.objects.get(slug=slug)
    tool_image_list = tool.images.all()
    publications_list = tool.publication_set.all()
    publication_list_published = publications_list.filter(status=2)
    tool_pros = tool.pros.split("|")
    tool_cons = tool.cons.split("|")
    context = {
                 'tool': tool,
                 'tool_images': tool_image_list,
                 'publications':publication_list_published,
                 'tool_pros': tool_pros,
                 'tool_cons': tool_cons,
               }
    return render(request, 'tool.html', context = context)


def blog(request, page=1):
    publications = Publication.objects.all()
    context = {'publications': publications }
    return render(request, 'blog.html', context=context)
