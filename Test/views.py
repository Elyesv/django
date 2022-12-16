from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Product
from .form import ProductForm 

# Create your views here.
def index(request):
    context = {
        'products': Product.objects.all,
    }
    return render(request,'apps/index.html', context)

def show(request, id):
    context ={
        'product': Product.objects.get(id = id)
    }
    return render(request, "apps/show.html", context)

def delete(request, id):
    product = get_object_or_404(Product, id = id)
    product.delete()
    
    return HttpResponseRedirect("/app")

def create(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/app")
         
    context={
        "form": form
    }    

    return render(request, "apps/create.html", context)

def update(request, id):
    context ={}
 
    obj = get_object_or_404(Product, id = id)
 
    form = ProductForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../show/"+id)
 
    context["form"] = form
 
    return render(request, "apps/update.html", context)