from django.shortcuts import render, redirect
from django.http import HttpResponse
from order_entry.forms import order_form
from order_entry.models import order

def odr(request):  
    if request.method == "POST":  
        form = order_form(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect(show)  
            except:  
                pass  
    else:  
        form = order_form()  
    return render(request,'index.html',{'form':form})  

def show(request):
    orders = order.objects.all()
    return render(request,"show.html",{'order_entry_order':orders})

def update(request, id):  
    orders = order.objects.get(id=id)  
    form = order_form(request.POST, instance = orders)  
    if form.is_valid():  
        form.save()  
        return redirect(show)  
    return render(request, 'edit.html', {'order': orders})  

def destroy(request, id):  
    orders = order.objects.get(id=id)
    orders.delete()
    return redirect(show)