from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('collection/',views.collection,name='collection'),
    path('shoes/',views.shoes,name='shoes'),
    path('racing_boots/',views.racing_boots,name='racing_boots'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('seller_add_product/',views.seller_add_product,name='seller_add_product'),
    path('seller_index/',views.seller_index,name='seller_index'),
    path('seller_view_product/',views.seller_view_product,name='seller_view_product'),
    path('seller_edit_product/<int:pk>/',views.seller_edit_product,name='seller_edit_product'),
    path('seller_product_detail/<int:pk>/',views.seller_product_detail,name='seller_product_detail'),
    path('seller_product_delete/<int:pk>/',views.seller_product_delete,name='seller_product_delete'),
    path('user_product_detail/<int:pk>/',views.user_product_detail,name='user_product_detail'),
    path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('mywishlist/',views.mywishlist,name='mywishlist'),
    path('remove_form_wishlist/<int:pk>/',views.remove_form_wishlist,name='remove_form_wishlist'),
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
    path('mycart/',views.mycart,name='mycart'),
    path('remove_form_cart/<int:pk>/',views.remove_form_cart,name='remove_form_cart'),
    path('change_qty/',views.change_qty,name='change_qty'),
    path('pay/',views.initiate_payment,name='pay'),
    path('callback/',views.callback, name='callback'),
    path('myorder/',views.myorder,name='myorder'),
    path('user_order_details/<int:pk>/',views.user_order_details,name='user_order_details'),
    path('user_product_search/',views.user_product_search,name='user_product_search'),
    path('login_validate_email/',views.login_validate_email,name='login_validate_email'),


]
