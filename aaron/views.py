import random
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from aaron.models import AaronPage, AaronsTag

# Create your views here.
# we need to pass this request
def AdaptiveGameView(request):
    context_object_name = 'Page'
    model = AaronPage
    postPages = []

    PATH = request.path
    GET = request.GET

    allPages = AaronPage.objects.all().values_list('id')
    thesePages = random.sample(list(allPages),2)
    for page in thesePages:
        postPages.append(AaronPage.objects.get(id=page[0]))


    program_headline = '<h1>Program Page</h1>'
    # context variables in the {} are accessible on home within {{}}
    return render(request,'aaron.html', {'GET':GET,'postPages':postPages})


# Create your views here.
# we need to pass this request
def AdaptiveGameTagView(request,tag,**kwargs):
    context_object_name = 'Page'
    model = AaronPage
    postPages = []

    if kwargs:
        template = 'aaron_' + str(kwargs['frames']) + '_.html' 
    else:
        template = 'aaron.html'

    PATH = request.path
    GET = request.GET
    thisTagID = AaronsTag.objects.get(tag=tag)
    allPages = AaronPage.objects.all().filter(tag=thisTagID).values_list('id')
    thesePages = random.sample(list(allPages),2)
    for page in thesePages:
        postPages.append(AaronPage.objects.get(id=page[0]))


    program_headline = '<h1>Program Page</h1>'
    # context variables in the {} are accessible on home within {{}}
    return render(request,template, {'GET':GET,'postPages':postPages})
