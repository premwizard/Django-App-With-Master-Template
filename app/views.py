from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'second.html')

def third(request):
    return render(request, 'Third.html')