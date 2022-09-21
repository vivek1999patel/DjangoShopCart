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
  path('all_products/<int:product_id>/', views.product_detail, name='product_detail'),
  path('product/create/', views.ProductCreate.as_view(), name='product_create'),
  path('all_products/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),


# order products by alphabet amd price
  path('products_decreasing/', views.order_by_decreasing_price, name='products_index_decreasing'),
  path('products_increasing/', views.order_by_increasing_price, name='products_index_increasing'),
  path('products_alphabetically_ordered/', views.order_by_alphabet, name='products_order_by_alphabet'),

  path('cart/', views.cart, name = 'cart' ),


]