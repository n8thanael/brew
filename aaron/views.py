from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.views.generic import View
from aaron.models import AaronPage

# Create your views here.
# we need to pass this request
def AdaptiveGameView(request):
    context_object_name = 'Page'
    model = AaronPage

    PATH = request.path
    GET = request.GET

    thisPage = AaronPage.objects.first()
    print(thisPage)

    program_headline = '<h1>Program Page</h1>'
    # context variables in the {} are accessible on home within {{}}
    return render(request,'aaron.html', {'GET':GET,'thisPage':thisPage})
