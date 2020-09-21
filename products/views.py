from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http.response import HttpResponse, JsonResponse
from django.http import FileResponse
import io
from .models import GiftModelForm, Gift


# Create your views here.
products = [
    {
        "id": 1,
        "name": "Tea pot",
        "brand": "Le Creuset",
        "price": "47.00GBP",
        "in_stock_quantity": 50
    },
    {
        "id": 2,
        "name": "Cast Iron Oval Casserole - 25cm; Volcanic",
        "brand": "Le Creuset",
        "price": "210.00GBP",
        "in_stock_quantity": 27
    },
    {
        "id": 4,
        "name": "Gordon Ramsay Maze 12 Piece Set, White",
        "brand": "ROYAL DOULTON",
        "price": "85.00GBP",
        "in_stock_quantity": 2
    },
    {
        "id": 5,
        "name": "9-speed Hand Mixer; Almond Cream",
        "brand": "KITCHENAID",
        "price": "99.99GBP",
        "in_stock_quantity": 9
    },
    {
        "id": 6,
        "name": "Mini Stand Mixer; Empire Red",
        "brand": "KITCHENAID",
        "price": "399.00GBP",
        "in_stock_quantity": 2
    },
    {
        "id": 7,
        "name": "50's Style Stand Mixer, Full-Colour White",
        "brand": "SMEG SMALL APPLIANCES",
        "price": "449.00GBP",
        "in_stock_quantity": 0
    },
    {
        "id": 8,
        "name": "50's Style Stand Mixer, Black",
        "brand": "SMEG SMALL APPLIANCES",
        "price": "449.99GBP",
        "in_stock_quantity": 1
    },
    {
        "id": 9,
        "name": "Polka Bedding Set, King, Silver",
        "brand": "BEAU LIVING",
        "price": "105.00GBP",
        "in_stock_quantity": 5
    },
    {
        "id": 10,
        "name": "Paignton Bedding Set, King, White",
        "brand": "BEAU LIVING",
        "price": "105.00GBP",
        "in_stock_quantity": 0
    },
    {
        "id": 11,
        "name": "Original Kettle E-5710 Charcoal Barbecue - 57cm; Black",
        "brand": "WEBER GRILLS",
        "price": "199.99GBP",
        "in_stock_quantity": 1
    },
    {
        "id": 12,
        "name": "Compact Charcoal Grill, 57 cm",
        "brand": "WEBER GRILLS",
        "price": "139.99GBP",
        "in_stock_quantity": 29
    },
    {
        "id": 13,
        "name": "Falcon T2 Square Parasol, 2.7m, Taupe",
        "brand": "GARDENSTORE",
        "price": "344.99GBP",
        "in_stock_quantity": 5
    },
    {
        "id": 14,
        "name": "Riva Round Parasol - 3m; Anthracite",
        "brand": "GARDENSTORE",
        "price": "79.99GBP",
        "in_stock_quantity": 8
    },
    {
        "id": 15,
        "name": "Glow Challenger T2 Square Parasol - 3m, Taupe",
        "brand": "GARDENSTORE",
        "price": "619.99GBP",
        "in_stock_quantity": 30
    },
    {
        "id": 16,
        "name": "Ceramic Bottle Lamp, Small",
        "brand": "THE WHITE COMPANY",
        "price": "95.00GBP",
        "in_stock_quantity": 0
    },
    {
        "id": 17,
        "name": "Gold Sitting Mouse Lamp",
        "brand": "GRAHAM & GREEN",
        "price": "73.00GBP",
        "in_stock_quantity": 3
    },
    {
        "id": 18,
        "name": "Usha Mango Wood Lamp Base",
        "brand": "NKUKU",
        "price": "49.95GBP",
        "in_stock_quantity": 12
    },
    {
        "id": 19,
        "name": "Sea Green Honeycomb Glass Lamp",
        "brand": "GRAHAM & GREEN",
        "price": "95.00GBP",
        "in_stock_quantity": 4
    },
    {
        "id": 20,
        "name": "Faux Tortoiseshell Lamp",
        "brand": "OKA",
        "price": "175.00GBP",
        "in_stock_quantity": 0
    },
    {
        "id": 21,
        "name": "2 Person Blue Tweed Hamper",
        "brand": "WILLOW STORE",
        "price": "85.50GBP",
        "in_stock_quantity": 4
    }
]


bought_product_list = []


def home(request):
    return render(request, 'products/home.html')


def view_all_products(request):
    return render(request, 'products/products.html', {'products': products})


def add_gift_to_list(request):
    if request.method == 'POST':
        form = GiftModelForm(request.POST)
        if form.is_valid():
            f_name = form.cleaned_data['name']
            f_brand = form.cleaned_data['brand']
            f_price = form.cleaned_data['price']
            f_stock = form.cleaned_data['stock']
            update_index = int(products[-1]['id']) + 1
            gifts = {'id': update_index,
                     'name': f_name,
                     'brand': f_brand,
                     'price': '{:.2f}GBP'.format(f_price),
                     'in_stock_quantity': f_stock,
                     }
            products.append(gifts)
            return render(
                request, 'products/products.html', {'products': products},
            )
    else:
        gift_class = GiftModelForm
        return render(
            request, 'products/add_product.html', {'form': gift_class},
        )


@csrf_exempt
def remove_gift_from_list(request):
    if request.method == 'POST':
        gift_name = request.POST["000202"]
        for index, product in enumerate(products):
            if product['name'] == gift_name or product['brand'] == gift_name:
                products.pop(index)
                return render(request,
                              "products/products.html",
                              {'products': products},)
    else:
        return return render(request,
                             "products/products.html",
                             {'notvalid': "Your request is not valid"})


@csrf_exempt
def product_to_buy_page(request):
    if request.method == 'POST':
        item_to_buy = request.POST['000202']
        json_obj = json.loads(item_to_buy)
        product = {
            'name': json_obj['name'],
            'brand': json_obj['brand'],
            'price': json_obj['price'].split('GBP')[0],
            'in_stock_quantity': json_obj['in_stock_quantity'],
        }

        return render(request,
                      'products/producttobuy.html',
                      {"product": product},)


def buy_product(request):

    if request.method == 'POST':
        form = GiftModelForm(request.POST)
        print(form)
        if form.is_valid():
            f_name = form.cleaned_data['name']
            f_brand = form.cleaned_data['brand']
            f_price = form.cleaned_data['price']
            f_quantity = int(form.cleaned_data['stock'])
            for index, gift in enumerate(products):
                if gift['name'] == f_name:
                    new_stock_quantity = gift['in_stock_quantity'] - f_quantity
                    buy_gifts = {'id': gift['id'],
                                 'name': f_name,
                                 'brand': f_brand,
                                 'price': '{:.2f}GBP'.format(
                        f_price * f_quantity),
                        'in_stock_quantity': f_quantity,
                    }
                    bought_product_list.append(buy_gifts)
                    products[index]['in_stock_quantity'] = new_stock_quantity
                    return render(request,
                                  "products/products.html",
                                  {'products': products})
        else:
            return render(request,
                          "products/products.html",
                          {'notvalid': "This is not a valid request"})


def view_product_report(request):
    product_report = []
    if request.method == 'GET':
        if bought_product_list:
            for index_one, bought_product in enumerate(bought_product_list):
                for index, item_name in enumerate(products):
                    if bought_product['name'] == item_name['name']:
                        item_name.update(
                            bought_item=bought_product['in_stock_quantity'])
                        product_report.append(item_name)

            return render(request,
                          'products/product_report.html',
                          {'reports': product_report})
        else:
            return render(request,
                          'products/product_report.html',
                          {'invalid': "No Report for Item purchased"})


def purchase_items(request):
    if request.method == 'GET':
        if bought_product_list:
            return render(request,
                          'products/purchase_item.html',
                          {'products': bought_product_list})
        else:
            return render(request,
                          'products/purchase_item.html',
                          {'noproduct': 'No gift have been purchased yet.'})
