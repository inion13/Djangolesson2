from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<int:item_id>', views.item, name='item'),
    path('items/', views.get_items, name='items'),
    path('about/', views.about, name='about'),
    path('fill/', views.fill, name='fill'),
    path('create/', views.create_item, name='create'),
    path('read/<int:item_id', views.read_item, name='read+ '),
    path('update/<int:item_id', views.update_item, name='update'),
    path('delete/<int:item_id', views.delete_item, name='delete')
]
