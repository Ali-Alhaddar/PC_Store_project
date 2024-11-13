from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    path('index/', views.index, name = 'index'),
    path('product/<int:product_id>/<str:product_type>/', views.detail, name='product_detail'),



    path('pcs/create', views.PcCreate.as_view(), name = 'Pcs_create'),
    path('pcs/<int:pk>/update/', views.PcUpdate.as_view(), name = 'pcs_update'),
    path('pcs/<int:pk>/delete/', views.PcDelete.as_view(), name = 'pcs_delete'),


    path('monitors/create', views.MonitorCreate.as_view(), name = 'monitors_create'),
    path('monitors/<int:pk>/update/', views.MonitorUpdate.as_view(), name = 'monitors_update'),
    path('monitors/<int:pk>/delete/', views.MonitorDelete.as_view(), name = 'monitors_delete'),


    path('keyboards/create', views.KeybordCreate.as_view(), name = 'keyboards_create'),
    path('keyboards/<int:pk>/update/', views.KeybordUpdate.as_view(), name = 'keyboards_update'),
    path('keyboards/<int:pk>/delete/', views.KeybordDelete.as_view(), name = 'keyboards_delete'),


    path('add/<str:model_name>/<int:object_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),

    
    path('accounts/signup/', views.signup, name='signup'),
]  