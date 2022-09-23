from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.ProductList.as_view(), name='home'),
  path('products/', views.products, name ='products'),
  path('user/',views.user, name='user'),

  # User SignIn/LogIn
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup/', views.signup, name='signup'),

  # Products
  path('all_products/', views.ProductList.as_view(), name='products_index'),
  path('all_products/<int:product_id>/', views.product_detail, name='product_detail'),
  path('product/create/', views.ProductCreate.as_view(), name='product_create'),
  path('all_products/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
  path('all_products/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),

  # Add-To-Cart
  path('all_product/<int:user_id>/assoc_product/<int:product_id>', views.assoc_product, name='assoc_product'),
  # Remove From Cart
  path('all_product/<int:user_id>/unassoc_product/<int:product_id>', views.unassoc_product, name='unassoc_product'),
  # Add-To-Cart When user is not logged in
  path('productLoggedInDetal/<int:product_id>/', views.product_loggedIn_detail, name='product_loggedIn_detail'),

  # Order products by alphabet amd price
  path('products/price=desc', views.order_by_decreasing_price, name='products_index_decreasing'),
  path('products/price=asc', views.order_by_increasing_price, name='products_index_increasing'),
  path('products/alphabet=asc', views.order_by_alphabet, name='products_order_by_alphabet'),
  path('products/alphabet=desc', views.order_by_alphabet_ztoa, name='products_order_by_alphabet_ztoa'),

  # Cart
  path('cart/', views.cart, name = 'cart' ),

  # Add Image
  path('all_product/<int:product_id>/add_photo/', views.add_photo, name='add_photo')


]