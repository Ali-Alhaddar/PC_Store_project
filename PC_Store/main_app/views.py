from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pc, CartItem
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class PcCreate(LoginRequiredMixin, CreateView):
    model = Pc
    fields = '__all__'

class PcUpdate(LoginRequiredMixin, UpdateView):
    model = Pc
    fields = '__all__'

class PcDelete(LoginRequiredMixin, DeleteView):
    model = Pc
    success_url = '/pcs/' 





def home(request):
        return render(request,'home.html')
    
def about(request):
        return render(request,'about.html')
login_required

def pcs_index(request):
    pcs = Pc.objects.all()
    return render(request, 'pc/index.html', {'pcs': pcs})
login_required
def pcs_detail(request, pc_id):
    pc = Pc.objects.get(id=pc_id)
    return render(request, 'pc/detail.html', {'pc': pc})

def view_cart(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if the user is not authenticated

    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.content_object.price * item.quantity for item in cart_items)
    return render(request, 'main_app/cart.html', {'cart_items': cart_items, 'total_price': total_price})
def add_to_cart(request, object_id):
    object = object.objects.get(id=object_id)
    cart_item, created = CartItem.objects.get_or_create(object=object, 
                                                       user=request.user)
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
            return redirect('index')
        else:
            error_message = 'Invalid Sign Up - Please Try Again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)