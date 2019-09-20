from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.Add.as_view(), name='add'),
  path('delete/<int:item_id>', views.delete, name='delete'),
]