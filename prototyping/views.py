from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404
from django.shortcuts import render,redirect
from django.core.mail import send_mail

from django.contrib.auth.forms import UserCreationForm

from .models import Tool, PrototypingTool, Link, Resource, Publication, Contact, Toolbox, Toolboxcategory, Conference, Video, Book

from .forms import ContactForm, SignUpForm
from django.http import HttpResponseRedirect

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            
            current_site = get_current_site(request)
            mail_subject = 'Activate your UXPRO account'
            message = render_to_string('acc_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()


            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('/activateyouraccount')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def activateyouraccount(request):
    return render(request, 'activate_your_account.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return redirect('/accountactive')
    else:
        return redirect('/invalidlink')

def accountactive(request):
    return render(request, 'account_active.html')

def invalidlink(request):
    return render(request, 'invalid_link.html')

def index(request,pagenumber = 1, tag = None):
    #publications_list_published = Publication.objects.filter(status=2)#order_by('-pub_date')
    filter_by_tag = False
    
    if tag is not None:
      links_list_published = Link.objects.filter(published=True, tags__slug=tag).order_by('-pub_date')
      filter_by_tag = True

    else:
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
    context = { 'links': links,
                'filter_by_tag': filter_by_tag,
                'tag': tag,
              }
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

def conferences(request):
    all_conferences = Conference.objects.filter(status=2).order_by('-from_date')
    context = {'all_conferences': all_conferences}
    return render(request, 'conferences.html', context = context)

def videos(request):
    all_videos = Video.objects.filter(status=2)
    context = {'all_videos': all_videos}
    return render(request, 'videos.html', context = context)

def books(request):
    all_books = Book.objects.filter(published=True)
    context = {'all_books': all_books}
    return render(request, 'books.html', context = context)

def prototyping(request):
    prototyping_tools = PrototypingTool.objects.filter(published=True)
    context = {'prototyping_tools': prototyping_tools}
    return render(request, 'prototyping.html', context = context)

def alltools(request):
    prototyping_tools = PrototypingTool.objects.filter(published=True)
    context = {'prototyping_tools': prototyping_tools}
    return render(request, 'tools_all.html', context = context)

def alltoolsinbox(request,category):
    category_clean = Toolboxcategory.objects.get(slug=category)
    box_tools = Toolbox.objects.filter(category=category_clean)
    context = {
                 'box_tools': box_tools,
                 'category': category_clean,
                 }
    return render(request, 'toolbox_all.html', context = context)


def toolboxtool(request, slug):
    tool = Toolbox.objects.get(slug=slug)
    context = {
                 'tool': tool,
               }
    return render(request, 'toolbox.html', context = context)




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
            #Contact.objects.create(**form.cleaned_data)

            subject = form.cleaned_data['full_name']
            message = form.cleaned_data['message']
            sender_email = form.cleaned_data['email']
            Contact.objects.create(full_name = subject,email=sender_email, message=message)
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

