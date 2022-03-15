from django.contrib import messages
from django.shortcuts import redirect, render
from .models import CustomUser, Customer, Seller
from .forms import CustomerCreationForm, SellerCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash


def RegisterView(request):
    form = CustomerCreationForm()
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emailverify')
    template_name = 'Accounts/Register.html'
    context = {'form': form}
    return render(request, template_name, context)


def LoginView(request):
    try:
        if request.method == 'POST':
            no = request.POST.get('mobile')
            p = request.POST.get('password')
            cuser = CustomUser.objects.get(mobile_no=no)
            print(cuser)
            if cuser:
                if cuser.is_active:
                    user = authenticate(username=no, password=p)
                    if user and user.is_customer:
                        login(request, user)
                        return redirect('customerhome')
                    else:
                        messages.error(request,
                                       'You entered invalid credential for mobile no.,password or you may not registered as a customer!!')
                        return redirect('login')
                else:
                    messages.error(request, 'Still you do not activate your account please activate it below!!')
                    return redirect('emailverify')
            else:
                messages.error(request, 'your are not register user plz register')
    except Customer.DoesNotExist:
        return redirect('logout')
    template_name = 'Accounts/Login.html'
    context = {}
    return render(request, template_name, context)


def ShowView(request):
    usr = Customer.objects.all()
    print(usr)
    template_name = 'Accounts/Show.html'
    context = {'user': usr}
    return render(request, template_name, context)


def LogoutView(request):
    logout(request)
    return redirect('customerhome')


def SellerRegisterView(request):
    form = SellerCreationForm()
    if request.method == 'POST':
        form = SellerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('selleremailverify')
    template_name = 'Accounts/SellerRegister.html'
    context = {'form': form}
    return render(request, template_name, context)


def SellerLoginView(request):
    try:
        if request.method == 'POST':
            no = request.POST.get('mobile')
            p = request.POST.get('password')
            try:
                suser = CustomUser.objects.get(mobile_no=no)

            except Seller.DoesNotExist:
                messages.error(request, 'your are not register plz register ')

                return redirect('slog')

            if suser:

                if suser.is_active:
                    user = authenticate(username=no, password=p)
                    if user and user.is_seller:
                        login(request, user)
                        return redirect('sellerhome')
                    else:

                        messages.error(request,'You entered invalid credintial for mobile no.,password or you may not registered as a Seller!!')
                        return redirect('sellerlogin')
                else:
                    messages.error(request, 'Still you do not activate your account please activate it below!!')
                    return redirect('selleremailverify')
            else:
                messages.error(request, 'your are not register plz register ')


    except Seller.DoesNotExist:
        return redirect('sellerlogout')
    template_name = 'Accounts/SellerLogin.html'
    context = {}
    return render(request, template_name, context)


def SellerShowView(request):
    usr = Seller.objects.all()
    print(usr)
    tempalte_name = 'Accounts/SellerShow.html'
    context = {'user': usr}
    return render(request, tempalte_name, context)


def SellerLogoutView(request):
    logout(request)
    return redirect('sellerhome')


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def send_otp(request):
    email = request.POST.get("email")
    print(email)
    o = generateOTP()
    print(o)
    htmlgen = 'Your OTP is ' + o
    send_mail('OTP request', htmlgen, 'taraleaish1029@gmail.com', [email], fail_silently=False)

    return HttpResponse(o)


def CustomerEmailVerificationview(request):
    template_name = 'Accounts/Customeremailverify.html'
    context = {}
    return render(request, template_name, context)


def Customeractivateview(request):
    try:
        email = request.POST.get('email')
        customer = CustomUser.objects.get(email=email)
        customer.is_active = True
        customer.save()
        return render('login')
    except Customer.DoesNotExist:
        return redirect('logout')


def SellerEmailVerificationview(request):
    template_name = 'Accounts/Selleremailverify.html'
    context = {}
    return render(request, template_name, context)


def Selleractivateview(request):
    try:
        email = request.POST.get('email')
        print(email)
        customer = CustomUser.objects.get(email=email)
        print(customer)
        customer.is_active = True
        print(customer.is_active)
        customer.save()
        return redirect('sellerlogin')
    except Seller.DoesNotExist:
        return redirect('sellerlogout')


def Customerpassview(request):
    form = SetPasswordForm(request.user)
    template_name = 'Accounts/Customerforgotpass.html'
    context = {'form': form}
    return render(request, template_name, context)


def Customerpasswordforgotview(request):
    try:
        print(request.POST)
        email = request.POST.get('email')
        print(email)
        customer = CustomUser.objects.get(email=email)
        print(customer)
        password = request.POST.get('new_password2')
        print(password)
        cnpass = str(password)
        customer.set_password(cnpass)
        customer.save()
        return redirect('customerhome')
    except Customer.DoesNotExist:
        return redirect('logout')


def Sellerpassview(request):
    form = SetPasswordForm(request.user)
    template_name = 'Accounts/Sellerforgotpass.html'
    context = {'form': form}
    return render(request, template_name, context)


def Sellerpasswordforgotview(request):
    try:
        print(request.POST)
        email = request.POST.get('email')
        print(email)
        seller = CustomUser.objects.get(email=email)
        print(seller)
        password = request.POST.get('new_password2')
        print(password)
        cnpass = str(password)
        seller.set_password(cnpass)
        seller.save()
        return redirect('sellerhome')
    except Seller.DoesNotExist:
        return redirect('sellerlogout')


def Customerchangepassview(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('customerhome')
        else:
            messages.error(request, 'Please check your password once!!')

    template_name = 'Accounts/Customerchangepass.html'
    context = {'form': form}
    return render(request, template_name, context)


def Sellerchangepassview(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('sellerhome')
        else:
            messages.error(request, 'Please check your password once!!')
    template_name = 'Accounts/Sellerchangepass.html'
    context = {'form': form}
    return render(request, template_name, context)

