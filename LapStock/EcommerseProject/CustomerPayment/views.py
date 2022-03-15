from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from Accounts.models import Customer
from Customer.models import Order_item
from Customer.models import Custorders
from django.http import FileResponse
from fpdf import FPDF


def CustomerRazorpayPayment(request):
    amount = 0
    user = request.user
    cst = Customer.objects.get(user=user)
    ord = Order_item.objects.filter(customer=cst)
    for i in ord:
        amount = amount+i.price
    amount = amount*100
    amount1 = amount/100
    if request.method == "POST":
        name = request.POST.get('name')
        client = razorpay.Client(
auth = ("rzp_test_E0TrRpVfHMc1l2", "JglS56dT94J1VWwZvbra6SSw"))
        payment = client.order.create({'amount': amount, 'currency': 'INR',
'payment_capture': '1'})

    return render(request, 'CustomerPayment/Placeorder.html', {'amount': amount, 'customer': cst, 'amount1': amount1})


@csrf_exempt
def CustomerRazorpayconfirm(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    ord =  Order_item.objects.filter(customer=customer)
    ord.delete()
    return render(request, "CustomerPayment/Confirmorder.html")


@login_required(login_url='login')
def report(request, id):
    user = request.user
    order = Custorders.objects.get(id=id)
    sales = []
    if bool(order.laptop):
        product = [
            {"title": "Member Name", "description": f'{order.fname} {order.lname}'},
            {"title": "Member Mobile No.", "description": f'{order.mobile_no}'},
            {"title": "Shipping Address/Billing Address", "description": f'{order.address}'},
            {"title": "Brand Name", "description":f'{order.laptop.brand_name}' },
            {"title": "Model Name", "description":f'{order.laptop.model_name}'},
            {"title": "Total Quantity", "description": f'{order.items}'},
            {"title": "Total Price", "description": f'{order.price}'},    
        ]
        sales.extend(product)


    elif bool(order.accessories):
        product = [
            {"title": "Member Name", "description": f'{order.fname} {order.lname}'},
            {"title": "Member Mobile No.", "description":f'{order.mobile_no}'},
            {"title": "Shipping Address/Billing Address", "description":f'{order.address}'},
            {"title":"Product Name", "description":f'{order.accessories.product_name}' },
            {"title": "Total Quantity", "description": f'{order.items}'},
            {"title": "Total Price", "description": f'{order.price}'},
        ]
        sales.extend(product)
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'LapStock Market  (Invoice For your order Item)',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Title'.ljust(30)} {'Description'.rjust(20)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)
    for line in sales:
        pdf.cell(200, 8, f"{line['title'].ljust(30)} {line['description'].rjust(20)}", 0, 1)
    pdf.output('report.pdf', 'F')
    return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

