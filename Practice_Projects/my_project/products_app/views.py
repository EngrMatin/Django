from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def fruits(request):
    delivery = {'district': ['Dhaka', 'Narayangonj', 'Gazipur', 'Munsiganj', 'Narsingdi', 'Cumilla', 'Brahmanbaria', 'Chandpur', 'Feni', 'Noakhali', 'Laxmipur', 'Chattogram']}
    return render(request, 'products/products.html', context = delivery)