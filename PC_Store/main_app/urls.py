from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('pcs/', views.pcs_index, name = 'index'),
    path('pcs/<int:pc_id>/', views.pcs_detail, name = 'detail'),
]