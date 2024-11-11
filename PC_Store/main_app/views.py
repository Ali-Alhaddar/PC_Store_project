from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pc
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

class PcCreate(CreateView):
    model = Pc
    fields = '__all__'

class PcUpdate(UpdateView):
    model = Pc
    fields = '__all__'

class PcDelete(DeleteView):
    model = Pc
    success_url = '/pcs/' 





def home(request):
        return render(request,'home.html')
    
def about(request):
        return render(request,'about.html')

def pcs_index(request):
    pcs = Pc.objects.all()
    return render(request, 'pc/index.html', {'pcs': pcs})

def pcs_detail(request, pc_id):
    pc = Pc.objects.get(id=pc_id)
    return render(request, 'pc/detail.html', {'pc': pc})

