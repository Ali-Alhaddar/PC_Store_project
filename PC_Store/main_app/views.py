from django.shortcuts import render
from .models import Pc 

# Create your views here.
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