from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Seller
from .forms import *
from django.contrib.auth.decorators import login_required
from Accounts.views import *
from django.contrib import messages


# @login_required(login_url='sellerlogin')
# def ProductView(request):
#     form = ProductForm()
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             seller = Seller.objects.get(user=request.user)
#             product.seller = seller
#             product.save()
#             return HttpResponse('Product Category Created!!!......')
#     template_name = 'Seller/Sellerproduct.html'
#     context = {'form': form}
#     return render(request, template_name, context)


@login_required(login_url='sellerlogin')
# @seller_required(login_url='sellerlogin')
def ProductView(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product1 = form.save(commit=False)
            selleruser = Seller.objects.get(user=request.user)
            product = Product.objects.filter(seller=selleruser)
            prdlist = []
            for prd in product:
                prdlist.append(prd.category_name)
            name = form.cleaned_data.get('category_name')
            if name in prdlist:
                messages.error(request, 'That Category is already present')
            else:
                product1.seller = selleruser
                form.save()
                messages.success(request, 'That Category Selected')
                return redirect('sellerhome')
    template_name = 'Seller/Sellerproduct.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='sellerlogin')
def Sellerlaptopview(request):
    form = Laptopform()
    if request.method == 'POST':
        form = Laptopform(request.POST, request.FILES)
        if form.is_valid():
            laptop = form.save(commit=False)
            selleruser = Seller.objects.get(user=request.user)
            product = Product.objects.filter(seller=selleruser)
            for prd in product:
                if prd.category_name == 'laptop':
                    laptop.product = prd
                    form.save()
                    return redirect('sellerinventory')
    template_name = 'Seller/Sellerlaptop.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url = 'sellerlogin')
def Selleraccessoriesview(request):
    form = AccessoriesForm()
    if request.method == 'POST':
        form = AccessoriesForm(request.POST, request.FILES)
        if form.is_valid():
            accessories = form.save(commit=False)
            selleruser = Seller.objects.get(user=request.user)
            x = Product.objects.filter(seller=selleruser)
            for i in x:
                if i.category_name == 'accessories':
                    accessories.product = i
                    form.save()
                    return redirect('sellerinventory')
    template_name = 'Seller/Selleraccessories.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='sellerlogin')
def Sellerinventoryview(request):
    selleruser = Seller.objects.get(user=request.user)
    product = Product.objects.filter(seller=selleruser)
    lap = None
    acce = None
    for prd in product:
        if prd.category_name == 'laptop':
            lap = Laptop.objects.filter(product=prd)
        elif prd.category_name == 'accessories':
            acce = Accessories.objects.filter(product=prd)
    template_name = 'Seller/Sellerinventory.html'
    context = {'lap': lap, 'acce': acce}
    return render(request, template_name, context)


@login_required(login_url='sellerlogin')
def Sellerlaptopupdateview(request, lapupdate):
    lap = Laptop.objects.get(id=lapupdate)
    form = Laptopform(instance=lap)
    if request.method == 'POST':
        form = Laptopform(request.POST, request.FILES, instance=lap)
        if form.is_valid():
            laptop = form.save(commit=False)
            selleruser = Seller.objects.get(user=request.user)
            product = Product.objects.filter(seller=selleruser)
            for prd in product:
                if prd.category_name == 'laptop':
                    laptop.product = prd
                    form.save()
                    return redirect('sellerinventory')
    template_name = 'Seller/Sellerlaptop.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='sellerlogin')
def Selleraccessoriesupdateview(request, groupdate):
    acce = Accessories.objects.get(id=groupdate)
    form = AccessoriesForm(instance=acce)
    if request.method == 'POST':
        form = AccessoriesForm(request.POST, request.FILES, instance=acce)
        if form.is_valid():
            accessories = form.save(commit=False)
            selleruser = Seller.objects.get(user=request.user)
            product = Product.objects.filter(seller=selleruser)
            for prd in product:
                if prd.category_name == 'accessories':
                    accessories.product = prd
                    form.save()
                    return redirect('sellerinventory')
    template_name = 'Seller/Selleraccessories.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='sellerlogin')
def Sellerlaptopdeleteview(request, lapdelete):
    lap = Laptop.objects.get(id=lapdelete)
    lap.delete()
    return redirect('sellerinventory')


@login_required(login_url='sellerlogin')
def Selleraccessoriesdeleteview(request, grodelete):
    gro = Accessories.objects.get(id=grodelete)
    gro.delete()
    return redirect('sellerinventory')


def Sellerhomeview(request):
    template_name = 'Seller/Sellerhome.html'
    context = {}
    return render(request, template_name, context)
