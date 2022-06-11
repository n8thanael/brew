from django.shortcuts import render

# Create your views here.
# we need to pass this request
def home(request):
    return render(request, 'home.html')

# Create your views here.
# we need to pass this request
def test(request):
    return render(request, 'test.html')