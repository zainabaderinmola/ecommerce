from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View, FormView, TemplateView
from django.http import JsonResponse
import json
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.views.generic import ListView, DetailView, View, FormView, TemplateView
from .models import *
from .utils import cookieCart, cartData, guestOrder
from django.core.mail import send_mail
from .forms import *

# Create your views here.
def home(request):
    data = cartData(request)
    cartItems = data['cartItems']

    context = {'cartItems':cartItems}
    return render(request, 'store/home.html', context)

def store(request, category_slug=None):
    data = cartData(request)
    cartItems = data['cartItems']
    
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    try:
        products = paginator.get_page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'page': page,'products': products, 'cartItems':cartItems,'category':category, 'categories':categories,}
    return render(request, 'store/store.html', context)


# class ItemDetailView(DetailView):
#     model = Product
#     template_name = 'store/product.html'

def product(request, slug):
    data = cartData(request)
    cartItems = data['cartItems']

    product = get_object_or_404(Product, slug=slug)
    context = {'cartItems':cartItems, 'product':product}
    return render(request, 'store/product.html', context)


def cart(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created =  Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity +=1
    elif action == 'remove':
        orderItem.quantity -=1
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


def subscribe(request):
    if request.methof == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Thank you for subscribing to our mailing list'
            message = 'Hi {}, we are pleased to have you on our subscription list'.format(cd['name'])
            recipient_list = [cd['to']]
            send_mail(subject, message,recipient_list, fail_silently=True)
            sent = True
    else:
        form = SubscriptionForm()
    return render(request, 'store/home.html')

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    items = data['items']
    print(items)
    

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created =  Order.objects.get_or_create(customer=customer, complete=False)
        

        
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
        #To the Buyer
        subject = 'Thank you for your patronage'
        message = f'Hi {customer.name}, thank you for patronising our market.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [customer.email,]
        send_mail(subject, message, email_from, recipient_list, fail_silently=True)
        
    order.save()

    if order.shipping == True:
        shipping_address = ShippingAddress.objects.create(
                customer=customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode'],
            )
        
        #To the seller
        subject = 'An order has been completed'
        message = f' {shipping_address.customer},with shipping address{ shipping_address.address } at { shipping_address} has made an order'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER,]
        send_mail(subject, message, email_from, recipient_list, fail_silently=True)

    return JsonResponse('Payment complete', safe=False)