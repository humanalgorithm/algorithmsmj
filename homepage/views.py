from django.shortcuts import render

def aboutus(request):
    return render(request, "aboutus.html")

def learnmore(request):
    return render(request, "learnmore.html")

def pythonabout(request):
    return render(request, "pythonabout.html")

def fourzerofour(request):
    return render(request, "404.html")

def home(request):
    return render(request, "sort.html")
