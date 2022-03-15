
from django.shortcuts import render, redirect
from Accounts.models import Customer
from .models import  City, Country, State, Address
from .forms import CustomerAddressForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


@login_required(login_url='login')
def CustomerAddressview(request):
    customer = Customer.objects.get(user=request.user)
    form = CustomerAddressForm()
    if request.method == 'POST':
        form = CustomerAddressForm(request.POST)
        print(request.POST)
        print('Before',form.is_valid())
        if form.is_valid():
            print('After',form.is_valid())
            obj = form.save(commit=False)
            obj.customer = customer
            obj.save()
            return redirect('showProfile')
    template_name = 'CustomerProfile/CustomerProfile.html'
    context = {'form': form}
    return render(request, template_name, context)


# AJAX
def load_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id)
    context = {'states': states}
    return render(request, 'CustomerProfile/Statelist.html', context)


def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id)
    context = {'cities': cities}
    return render(request, 'CustomerProfile/Citylist.html', context)


@login_required(login_url='login')
def showProfile(request):
    customer = Customer.objects.get(user=request.user)
    customer_profile = Address.objects.filter(customer=customer)
    return render(request, 'CustomerProfile/ShowProfile.html', {'customer_profile':customer_profile})


# def update_Profile(request, pk):
#     customer = Customer.objects.get(user=request.user)
#     address = Address.objects.get(id=pk)
#     print('address:',address,address.country.id)
#     form = CustomerAddressForm(instance=address)
#     print('form',form)
#     if request.method == 'POST':

#         form = CustomerAddressForm(request.POST, instance=address)
#         print(request.POST)
#         print('Before',form.is_valid())
#         if form.is_valid():
#             print('After',form.is_valid())
#             obj = form.save(commit=False)
#             obj.customer = customer
#             obj.save()
#             return redirect('home2')
#     template_name = 'CustomerProfile/CustomerProfile.html'
#     context = {'form': form}
#     return render(request, template_name, context)


def deleteProfile(request, pk):
    customer_profile = Address.objects.get(id=pk)
    customer_profile.delete()
    return redirect('showProfile')


@method_decorator(login_required, name='put')
class CustomerAddressUpdateView(UpdateView):
    model = Address
    fields = ('fname', 'lname', 'mobile', 'country', 'state', 'city', 'address', 'address_type')
    success_url = reverse_lazy('showProfile')
    template_name ='CustomerProfile/CustomerProfile.html'
    
