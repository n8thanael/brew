from django.shortcuts import render

# Create your views here.
# we need to pass this request
def home(request):
    var = "Home"
    # context variables in the {} are accessible on home within {{}}
    return render(request, 'home.html',{'var':var,})