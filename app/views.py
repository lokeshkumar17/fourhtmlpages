from django.shortcuts import render
def h1(request):
    return render(request,'h1.html')

def h2(request):
    return render(request,'h2.html')

def h3(request):
    return render(request,'h3.html')

def h4(request):
    return render(request,'h4.html')

# Create your views here.
