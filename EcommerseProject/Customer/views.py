from django.shortcuts import redirect, render
from Accounts.models import Customer
from .models import Order_item
from Seller.models import Accessories,Laptop,Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import LaptopFilter, AccessoriesFilter
from .models import Custorders
from .forms import Ordersform
from CustomerProfile.models import Address


def HomeView(request):
    template_name = 'Customer/Home.html'
    context = {}
    return render(request, template_name, context)


@login_required(login_url='login')
def Laptopview(request, pk):
    laptop = Laptop.objects.get(id=pk)
    user = request.user
    try:
        cst = Customer.objects.get(user=user)
        y = Order_item.objects.filter(customer=cst, laptop=laptop).first()
        if y:
            z = y.quantity+1
            p = y.price/y.quantity
            q = p*z
            y.price = q
            y.quantity = z
            y.save()
            print('Updated!!!')
            return redirect('cartview')
        else:
            Order_item.objects.create(customer=cst, laptop=laptop, accessories=None, price=laptop.price, quantity=1)
            print('Created!!!')
        return redirect('cartview')
    except Customer.DoesNotExist:
        return redirect('login')


@login_required(login_url='login')
def Accessoriesview(request, pk):
    accessories = Accessories.objects.get(id=pk)
    user = request.user
    try:
        cst = Customer.objects.get(user=user)
        y = Order_item.objects.filter(customer=cst, accessories=accessories).first()
        if y:
            z = y.quantity+1
            p = y.price/y.quantity
            q = p*z
            y.price = q
            y.quantity = z
            y.save()
            print('Updated!!!')
            return redirect('cartview')
        else:
            Order_item.objects.create(customer=cst, laptop=None, accessories=accessories, price=accessories.price, quantity=1)
            print('Created!!!')
        return redirect('cartview')
    except Customer.DoesNotExist:
        return redirect('login')


@login_required(login_url='login')
def Cartview(request):
    user = request.user
    try:
        cst = Customer.objects.get(user=user)
        ord = Order_item.objects.filter(customer=cst)
        price = 0
        for i in ord:
            price = price+i.price
        print(len(ord))
        tord = len(ord)
        template_name = 'Customer/Cartview.html'
        context = {'ord': ord, 'tord': tord, 'price': price}
        return render(request, template_name, context)
    except Customer.DoesNotExist:
        return redirect ('logout')


@login_required(login_url='login')
def Deleteitemview(request, pk):
    # item = Order_item.objects.get(id=pk)
    # item.delete()
    # return redirect('cartview')
    y = Order_item.objects.get(id=pk)
    if y.quantity>1:
        z = y.quantity-1
        p = y.price/y.quantity
        q = p*z
        y.price = q
        y.quantity = z
        y.save()
        print('Updated!!!')
        return redirect('cartview')
    else:
        print('Deleted!!')
        y.delete()
    return redirect('cartview')


def Updateallitemview(request, pk):
    y = Order_item.objects.filter(id=pk).first()
    if y:
        z = y.quantity+1
        p = y.price/y.quantity
        q = p*z
        y.price = q
        y.quantity = z
        y.save()
        print('Updated!!!')
        return redirect('cartview')


def showlaptop(request):
    records = Laptop.objects.all()
    laptopfilter = LaptopFilter(request.GET, queryset=records)
    rec_per_page = Paginator(laptopfilter.qs, 3)
    page = request.GET.get('page', 1)
    # print('PAGE=',page)
    # print(rec_per_page.count)
    # print(rec_per_page.num_pages)
    # print(rec_per_page.page_range)
    try:
        rec = rec_per_page.page(page)
    except PageNotAnInteger:
        rec = rec_per_page.page(1)
    except EmptyPage:
        rec = rec_per_page.page(rec_per_page.num_pages)
    print('filter record', records)
    return render(request, 'Customer/ShowLaptop.html', {'records': rec, 'laptopfilter': laptopfilter})


def showAccessories(request):
    records = Accessories.objects.all()
    groceryfilter = AccessoriesFilter(request.GET, queryset=records)
    rec_per_page = Paginator(AccessoriesFilter.qs, 3)
    print('PAGINATOR=', rec_per_page)

    page=request.GET.get('page', 1)
    print('PAGE=',page)
    print(rec_per_page.count)
    print(rec_per_page.num_pages)
    print(rec_per_page.page_range)

    try:
        rec = rec_per_page.page(page)
    except PageNotAnInteger:
        rec = rec_per_page.page(1)
    except EmptyPage:
        rec = rec_per_page.page(rec_per_page.num_pages)

    return render(request, 'Customer/ShowAccessories.html', {'records':rec, 'AccessoriesFilter':AccessoriesFilter})


@login_required(login_url='login')
def Customerordersview(request):
    total = 0
    customer = Customer.objects.get(user=request.user)
    address = Address.objects.filter(customer=customer)
    order_item1 = Order_item.objects.filter(customer=customer)
    print(order_item1)
    cartitems = len(order_item1)
    for i in order_item1:
        total = total+i.price
        print(i.price)
        print(bool(i.laptop))
        print(type(i.laptop))
    form = Ordersform()
    form.fields['address'].queryset = address
    if request.method == 'POST':
        print(request.POST)
        add = request.POST.get('address')
        add1 = Address.objects.get(id=add)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        mobi = request.POST.get('mobile_no')
        date = request.POST.get('date')
        for i in order_item1:
            if bool(i.laptop):
                order = Custorders.objects.create(customer=customer, address=add1, fname=fname, lname=lname, laptop=i.laptop, price=i.price, items=i.quantity, mobile_no=mobi, date=date)

            elif bool(i.accessories):
                order = Custorders.objects.create(customer=customer, address=add1, fname=fname, lname=lname, accessories=i.accessories, price=i.price, items=i.quantity, mobile_no=mobi, date=date)
            # order.order_item.add(i)  
        return redirect('customerrazorpay')
    template_name = 'Customer/Orders.html'
    context = {'form': form, 'total': total, 'cartitems': cartitems,'address':address}
    return render(request, template_name, context)


@login_required(login_url='login')
def Customerorderlistview(request):
    customer = Customer.objects.get(user=request.user)
    orderlist = Custorders.objects.filter(customer=customer)
    print(orderlist)
    totalorderitems = len(orderlist)
    template_name = 'Customer/Customerorderslist.html'
    context = {'orderlist': orderlist, 'totalorderitems': totalorderitems}
    return render(request, template_name, context)



