from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('pcs/', views.pcs_index, name = 'index'),
    path('pcs/<int:pc_id>/', views.pcs_detail, name = 'detail'),

    path('pcs/create', views.PcCreate.as_view(), name = 'Pcs_create'),
    path('pcs/<int:pk>/update/', views.PcUpdate.as_view(), name = 'pcs_update'),
    path('pcs/<int:pk>/delete/', views.PcDelete.as_view(), name = 'pcs_delete'),
    path('cart/', views.view_cart, name = 'cart'),
    path('add/<int:object_id>/', views.add_to_cart, name='add_to_cart'),
    path('accounts/signup/', views.signup, name='signup'),
]  