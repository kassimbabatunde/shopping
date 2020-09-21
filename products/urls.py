from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_products', views.view_all_products, name='view_all_products'),
    path('add_gift', views.add_gift_to_list, name='add_gift'),
    path('remove_gift', views.remove_gift_from_list, name='remove_gift'),
    path('gift_to_buy', views.product_to_buy_page, name='gift_to_buy'),
    path('buy_product', views.buy_product, name='buy_product'),
    path('product_report', views.view_product_report,
         name='product_report'),

    path('purchase_items', views.purchase_items,
         name='purchase_items'),
]
