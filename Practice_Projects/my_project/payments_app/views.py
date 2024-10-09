from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def bkash(request):
    payment_method = 'bKash'
    discount = '30%'
    condition = 'For first payment only'
    payment_info = {'pm':payment_method, 'dis':discount, 'con':condition}
    return render(request, 'payments/payments-1.html', context = payment_info)

def rocket(request):
    return render(request, 'payments/payments-2.html')
