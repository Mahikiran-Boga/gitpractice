from django.shortcuts import render
def index(request):
    return render(request,"index.html")

# Create your views here.
def home(request):
    return render(request,"home.html")