from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pc, CartItem, Monitor, Keybord
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator



# Create your views here.

class PcCreate(LoginRequiredMixin, CreateView):
    model = Pc
    fields = '__all__'

class PcUpdate(LoginRequiredMixin, UpdateView):
    model = Pc
    fields = '__all__'

class PcDelete(LoginRequiredMixin, DeleteView):
    model = Pc
    success_url = '/' 



class MonitorCreate(LoginRequiredMixin, CreateView):
    model = Monitor
    fields = '__all__'

class MonitorUpdate(LoginRequiredMixin, UpdateView):
    model = Monitor
    fields = '__all__'

class MonitorDelete(LoginRequiredMixin, DeleteView):
    model = Monitor
    success_url = '/'




class KeybordCreate(LoginRequiredMixin, CreateView):
    model = Keybord
    fields = '__all__'

class KeybordUpdate(LoginRequiredMixin, UpdateView):
    model = Keybord
    fields = '__all__'

class KeybordDelete(LoginRequiredMixin, DeleteView):
    model = Keybord
    success_url = '/'





def home(request):
        return render(request,'home.html')
    
def about(request):
        return render(request,'about.html')
login_required

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
login_required
def detail(request, product_id, product_type):
    # Check the product type and fetch the relevant product
    if product_type == 'pc':
        product = get_object_or_404(Pc, id=product_id)
        delete_url_name = 'pcs_delete'
    elif product_type == 'monitor':
        product = get_object_or_404(Monitor, id=product_id)
        delete_url_name = 'monitors_delete'
    elif product_type == 'keyboard':
        product = get_object_or_404(Keybord, id=product_id)
        delete_url_name = 'keyboards_delete'
    else:
        return HttpResponse("Invalid product type.", status=400)
    
    # Return the product details to the template
    return render(request, 'store/detail.html', {
        'product': product,
        'delete_url_name': delete_url_name,
    })

def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if the user is not authenticated

    # Fetch all cart items for the authenticated user
    cart_items = CartItem.objects.filter(user=request.user)
    
    # Calculate the total price of all cart items
    total_price = sum(item.content_object.price * item.quantity for item in cart_items)

    # Pass the cart items and total price to the template
    return render(request, 'main_app/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def add_to_cart(request, product_id, product_type):
    
    if product_type == 'pc':
        product = get_object_or_404(Pc, id=product_id)
    elif product_type == 'monitor':
        product = get_object_or_404(Monitor, id=product_id)
    elif product_type == 'keyboard':
        product = get_object_or_404(Keybord, id=product_id)
    else:
        return redirect('index')  # Handle invalid product type
    
    # Add the product to the cart
    content_type = ContentType.objects.get_for_model(product)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=product.id,
    )
    
    # Increment quantity if the item is already in the cart
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')

def remove_from_cart(request, object_id):
    cart_object = CartItem.objects.get(id=object_id)
    cart_object.delete()
    return redirect('view_cart')

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