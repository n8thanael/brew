from django.shortcuts import render

# Create your views here.
# we need to pass this request
def aaron(request):
    return render(request, 'aaron.html')