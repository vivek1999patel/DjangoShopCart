from django.shortcuts import render,redirect

# Create your views here.
def home (request):
    return render(request, 'home.html')
def products(request):
    return render(request,'shop/index.html')