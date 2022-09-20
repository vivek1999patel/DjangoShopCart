from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('products/', views.products, name ='products'),
  path('user/',views.user, name='user'),

  # User SignIn/LogIn
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup/', views.signup, name='signup'),

  #products
  path('all_products/', views.ProductList.as_view(), name='products_index'),

  ]