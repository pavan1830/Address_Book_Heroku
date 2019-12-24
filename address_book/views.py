from django.shortcuts import render,redirect
from .models import addressModel
from .forms import addressForm
from django.contrib import messages
# Create your views here.
def home(request):
    all_address = addressModel.objects.all
    return render(request,'home.html',{'all_address':all_address})
def add_address(request):
    if request.method == 'POST':
        form = addressForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('Address Has Been Added'))
            return redirect('home')
        else:
            messages.success(request,('Seems Like Error Occured'))
            return render(request,'add_address.html',{})
    else:
        return render(request,'add_address.html',{})
def edit(request,list_id):
    if request.method == 'POST':
        current_address = addressModel.objects.get(pk = list_id)
        form = addressForm(request.POST or None, instance = current_address)
        if form.is_valid():
            form.save()
            messages.success(request,('Address Has Been Edited'))
            return redirect('home')
        else:
            messages.success(request,('Seems Like Error Occured'))
            return render(request,'edit.html')
    else:
        get_address = addressModel.objects.get(pk = list_id)
        return render(request,'edit.html',{'get_address': get_address})
def delete(request,list_id):
    if request.method == 'POST':
        current_address = addressModel.objects.get(pk = list_id)
        current_address.delete()
        messages.success(request,("Address Deleted"))
        return redirect('home')
    else:
        messages.success(request,("Nothing To See Here"))
        return render(request,'home')