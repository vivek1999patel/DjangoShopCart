# from django.shortcuts import render,redirect
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Cart
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import datetime

# Create your views here.
def home (request):
    prod = Product.objects.all()
    print(prod)
    return render(request, 'home.html')
def products(request):
    return render(request,'shop/index.html')
def user(request):
    return render(request,'shop/user/index.html')

def signup(request):
  error_message = ''

  if request.method == 'POST':
    form = UserCreationForm(request.POST)

    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')

    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ProductList(ListView):
    model = Product

class ProductCreate(LoginRequiredMixin, CreateView):
  model = Product
  fields = '__all__'




def order_by_alphabet(request):

  productList = Product.objects.all().order_by('name')

  return render(request, 'main/order_by_product_price_or_alphabet.html', {
    "productList": productList
  })


def order_by_decreasing_price(request):

  productList = Product.objects.all().order_by('-price')

  return render(request, 'main/order_by_product_price_or_alphabet.html', {
    "productList": productList
  })

def order_by_increasing_price(request):

  productList = Product.objects.all().order_by('price')

  return render(request, 'main/order_by_product_price_or_alphabet.html', {
    "productList": productList
  })