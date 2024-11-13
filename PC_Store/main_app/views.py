from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pc, CartItem, Monitor, Keybord
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.contrib import messages



# Create your views here.

class PcCreate(LoginRequiredMixin, CreateView):
    model = Pc
    fields = '__all__'
    success_url = '/'

class PcUpdate(LoginRequiredMixin, UpdateView):
    model = Pc
    fields = '__all__'
    success_url = '/'

class PcDelete(LoginRequiredMixin, DeleteView):
    model = Pc
    success_url = '/' 



class MonitorCreate(LoginRequiredMixin, CreateView):
    model = Monitor
    fields = '__all__'
    success_url = '/'

class MonitorUpdate(LoginRequiredMixin, UpdateView):
    model = Monitor
    fields = '__all__'
    success_url = '/'

class MonitorDelete(LoginRequiredMixin, DeleteView):
    model = Monitor
    success_url = '/'




class KeybordCreate(LoginRequiredMixin, CreateView):
    model = Keybord
    fields = '__all__'
    success_url = '/'


class KeybordUpdate(LoginRequiredMixin, UpdateView):
    model = Keybord
    fields = '__all__'
    success_url = '/'

class KeybordDelete(LoginRequiredMixin, DeleteView):
    model = Keybord
    success_url = '/'





def home(request):
        return render(request,'home.html')
    
def about(request):
        return render(request,'about.html')


def index(request):
    pcs = Pc.objects.all()
    monitors = Monitor.objects.all()
    keyboards = Keybord.objects.all()
    

    # Pagination
    paginator = Paginator(pcs, 10) 
    page = request.GET.get('page')
    pcs_page = paginator.get_page(page)

    paginator = Paginator(monitors, 10)
    monitors_page = paginator.get_page(page)

    paginator = Paginator(keyboards, 10) 
    keyboards_page = paginator.get_page(page)

   

    return render(request, 'store/index.html', {
        'pcs': pcs_page,
        'monitors': monitors_page,
        'keyboards': keyboards_page,
        
    })

def detail(request, product_id, product_type):
    if product_type == 'pc':
        product = get_object_or_404(Pc, id=product_id)
        model_name = 'pc'
    elif product_type == 'monitor':
        product = get_object_or_404(Monitor, id=product_id)
        model_name = 'monitor'
    elif product_type == 'keyboard':
        product = get_object_or_404(Keybord, id=product_id)
        model_name = 'keyboard'
   
    return render(request, 'store/detail.html', {
        'product': product,
        'model_name': model_name 
    })

def view_cart(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to view your cart.")
        return redirect('login')

    cart_items = CartItem.objects.filter(user=request.user)

    
    total_price = 0
    for cart_item in cart_items:
        product = cart_item.content_object 
        cart_item.total_price = product.price * cart_item.quantity
        total_price += cart_item.total_price  

    return render(request, 'main_app/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def add_to_cart(request, model_name, object_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to add items to the cart.")
        return redirect('login')

    if model_name == 'pc':
        product = get_object_or_404(Pc, id=object_id)
        content_type = ContentType.objects.get_for_model(Pc)
    elif model_name == 'monitor':
        product = get_object_or_404(Monitor, id=object_id)
        content_type = ContentType.objects.get_for_model(Monitor)
    elif model_name == 'keyboard':
        product = get_object_or_404(Keybord, id=object_id)
        content_type = ContentType.objects.get_for_model(Keybord)
    else:
        messages.error(request, 'Invalid product type')
        return redirect('home')

    
    cart_item, created = CartItem.objects.get_or_create(
        content_type=content_type,
        product_id=object_id,
        user=request.user,
        defaults={'quantity': 1}
    )

   
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f'{product.name} added to cart!')
    return redirect('cart')
def remove_from_cart(request, object_id):
    cart_object = CartItem.objects.get(id=object_id)
    cart_object.delete()
    return redirect('view_cart')


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid Sign Up - Please Try Again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)