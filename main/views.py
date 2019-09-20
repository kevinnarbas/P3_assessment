from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import WishList

# Create your views here.

def index(request):
  wishes = WishList.objects.all()
  return render(request, 'index.html', {'wishes': wishes})

def delete(request, item_id):
  WishList.objects.filter(id=item_id).delete()
  return redirect('index')
  

class Add(CreateView):
  model = WishList
  fields = '__all__'
