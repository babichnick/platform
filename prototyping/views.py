from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404
from django.shortcuts import render
from django.core.mail import send_mail

from django.contrib.auth.forms import UserCreationForm

from .models import Tool, PrototypingTool, Link, Resource, Publication, Contact

from .forms import ContactForm, SignUpForm
from django.http import HttpResponseRedirect


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def index(request,pagenumber = 1):
    #publications_list_published = Publication.objects.filter(status=2)#order_by('-pub_date')
    
    links_list_published = Link.objects.filter(published=True).order_by('-pub_date')
    paginator = Paginator(links_list_published, 12) #Show 12 latest publications

    links = paginator.get_page(pagenumber)

    
    #if page:
    #    context = {'publications': publications }
    #    return render(request, 'index_paginated.html', context=context)
    #else:
    #    head_post = publications[0]
    #    first_six_posts = publications[1:7]
    #    second_six_posts = publications[7:13]
    #    tail_post = publications[13]
    context = { 'links': links}
    #            'firstsixposts': first_six_posts,
    #            'secondsixposts': second_six_posts,
    #            'tailpost': tail_post,


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

def allresources(request):
    resources = Resource.objects.filter(published=True)
    context = {'resources': resources}
    return render(request, 'resources_all.html', context = context)

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

def about(request):
    return render(request, 'about.html')

def contact_me(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            Contact.objects.create(**form.cleaned_data)

            subject = form.cleaned_data['full_name']
            message = form.cleaned_data['message']
            sender = 'hello@uxpro.cc'
            recipients = ['nick@babich.biz']

            send_mail(subject, message, sender, recipients)
            
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def blog(request, page=1):
    publications = Publication.objects.all()
    context = {'publications': publications }
    return render(request, 'blog.html', context=context)

