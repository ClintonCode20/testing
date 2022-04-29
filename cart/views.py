from django.shortcuts import render
from .models import Product, Cart, Cartitems
from django.http import JsonResponse
import json
# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cart = []
        cart = {'quantity': 0}
        cartitems = []
    products = Product.objects.all()
    context = {'products': products, 'cart': cart, 'cartitems': cartitems}
    return render(request, 'cart/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        cart, created = Cart.objects.get_or_create(owner = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    context = {'cart': cart, 'cartitems': cartitems}
    return render(request, 'cart/cart.html', context)

def updateCart(request):
    data = json.loads(request.body)
    product_id = data['id']
    action = data['action']
    if request.user.is_authenticated:
        customer = request.user
        product = Product.objects.get(product_id =product_id)
        cart, created=Cart.objects.get_or_create(owner=request.user, completed=False)
        cartitems, created = Cartitems.objects.get_or_create(cart=cart, product=product)

        if action == 'add':
            cartitems.quantity += 1
        cartitems.save()

        msg = {
            'qty': cart.quantity,

        }
    return JsonResponse(msg, safe=False)

def updateQuantity(request):
    data = json.loads(request.body)
    product_id = data['id']
    inputvalue = int(data['val'])
    if request.user.is_authenticated:
        customer = request.user
        product = Product.objects.get(product_id =product_id)
        cart, created=Cart.objects.get_or_create(owner=request.user, completed=False)
        cartitems, created = Cartitems.objects.get_or_create(cart=cart, product=product)

        cartitems.quantity = inputvalue
        cartitems.save()

        msg = {
            'price': cartitems.product.price,
            'qty': cartitems.quantity,
            'grandtotal': cart.total,
            'subtotal': cartitems.subtotal,
            'quantity': cart.quantity
        }
    return JsonResponse(msg, safe=False)
