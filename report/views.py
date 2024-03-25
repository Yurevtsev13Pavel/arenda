from django.shortcuts import render
from datetime import datetime
from report.models import Order


# Create your views here.
def first_page(request):
    all_time = ['08:00', '09:00', '10:00', '11:00',
                '12:00', '13:00', '14:00', '15:00',
                '16:00', '17:00', '18:00', '19:00',]

    yesterday = datetime.today()

    dict_obj = {}
    return render(request, './index.html', dict_obj)

def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name = name, order_phone = phone)
        element.save()
        return render(request, './thanks.html', { 'name': name,})
    else:
        return render(request, './thanks.html')