from django.http.response import HttpResponse
from django.shortcuts import render
from Seller.models import Laptop, Accessories
from django.db.models import Q


def Search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        search1 = search.capitalize()
        searchsplit = search.split(' ')
        if search1 == 'Laptop':
            laptop = Laptop.objects.all()
            print(laptop)
            print('')
            template_name = 'UniversalSearch/Universalsearch.html'
            context = {'laptop': laptop}
            return render(request, template_name, context)

        elif search1 == 'Accessories':
            accessories = Accessories.objects.all()
            print(accessories)
            print('')
            template_name = 'UniversalSearch/Universalsearch.html'
            context = {'accessories': accessories}
            return render(request, template_name, context)
        else:
            laplist = []
            for i in searchsplit:
                lap = Laptop.objects.filter(
                    Q(model_name__icontains=i) | Q(brand_name__icontains=i) | Q(ram__icontains=i) | Q(
                        rom__icontains=i) | Q(processor__icontains=i))
                laplist.extend(lap)
            lapset = set(laplist)
            print(lapset)

            accelist = []
            for i in searchsplit:
                acce = Accessories.objects.filter(Q(product_name__icontains=i) | Q(price__icontains=i))
                accelist.extend(acce)
            acceset = set(accelist)
            print(acceset)
            if bool(lapset or  acceset) == False:
                blank = 'Record is not Found!!!!!!!'

                template_name = 'UniversalSearch/Universalsearch.html'
                context = {'blank': blank}
                return render(request, template_name, context)
            else:
                print('else')
                template_name = 'UniversalSearch/Universalsearch.html'
                context = {'lapset': lapset, 'acceset': acceset}
                return render(request, template_name, context)
    template_name = 'UniversalSearch/Universalsearch.html'
    context = {}
    return render(request, template_name, context)









