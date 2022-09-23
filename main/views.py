from main.forms import LoginForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Cart, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import datetime
import uuid
import boto3

S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'backendgrocery'

# Create your views here.
def home (request):
    prod = Product.objects.all()
    print(prod)
    return render(request,'main/product_list.html')

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

# List All Products
class ProductList(ListView):
  model = Product

# Create Product
class ProductCreate(LoginRequiredMixin, CreateView):
  model = Product
  fields = '__all__'

# Product Details
def product_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  userId = request.user.id

  return render(request, 'product/detail.html', {
    'product': product,
    'userId': userId
  })

# Update Product
class ProductUpdate(LoginRequiredMixin, UpdateView):
  model  = Product
  fields = ['name', 'price', 'desc', 'quantity']

# Delete Product
class ProductDelete(LoginRequiredMixin, DeleteView):
  model       = Product
  success_url = '/all_products/'

# Add To Cart Product
def assoc_product(request, user_id, product_id):
  cart = Cart.objects.filter(user_id=user_id)
  if cart:
    print(cart)
  else:
    c = Cart(user_id=user_id)
    c.save()

  Cart.objects.get(user_id=user_id).product.add(product_id)
  return redirect('cart')

# Remove From Cart
def unassoc_product(request, user_id, product_id):
    Cart.objects.get(user_id=user_id).product.remove(product_id)
    return redirect('cart')

# Add-To-Cart When User Is Not Logged In
@login_required
def product_loggedIn_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    userId  = request.user.id

    return render(request, 'product/detail.html', {
        'product': product,
        'userId': userId
    })

def order_by_alphabet(request):
  productList = Product.objects.all().order_by('name')
  return render(request, 'main/order_by_product_price_or_alphabet.html', {
    "productList": productList
  })
def order_by_alphabet_ztoa(request):
  productList = Product.objects.all().order_by('-name')
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

@login_required
def cart(request):
    userId = request.user.id
    current_user = request.user.id
    exist = Cart.objects.filter(user_id = current_user)
    
    if exist:
      print(exist)
    else:
      c = Cart(user_id = current_user)
      c.save()

    cart= Cart.objects.get(user_id = current_user)
    return render(request, 'product/cart.html', {'cart': cart, 'userId': userId})

# Add Image
def add_photo(request, product_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, product_id=product_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('products_index')

    #-*- coding: utf-8 -*-

