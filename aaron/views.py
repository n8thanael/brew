from django.shortcuts import render
from aaron.models import AaronPage

# Create your views here.
# we need to pass this request
def aaron(request):
    thisPage = AaronPage.objects.all()
    print(thisPage)
    context = 'something'
    return render(request, 'aaron.html', context)