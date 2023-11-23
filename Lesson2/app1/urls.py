from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<int:item_id>', views.item, name='item'),
    path('items/', views.get_items, name='items'),
    path('about/', views.about, name='about')
]
