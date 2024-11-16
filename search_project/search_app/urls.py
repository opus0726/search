
 
 
 
 
 
 
 
 
 
 
from django import forms 
from .models import Product 
 
class SearchForm(forms.Form): 
    query = forms.CharField( 
        label='検索キーワード', 
        max_length=100, 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': '検索したいキーワードを入力'})    
    ) 
 
class ProductForm(forms.ModelForm): 
    class Meta: 
        model = Product 
        fields = ['name', 'description', 'price', 'category']  
from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('', views.search_view, name='search_view'), 
    path('search/', views.search_view, name='search_view'), 
    path('product/new/', views.product_create, name='product_create'), 
    path('product/<int:pk>/', views.product_detail, name='product_detail'), 
    path('product/<int:pk>/edit/',  views.product_update, name='product_update'), 
    path('product/<int:pk>/delete',  views.product_delete, name='product_delete'), 
    path('product/', views.product_list, name='product_list'), 
]