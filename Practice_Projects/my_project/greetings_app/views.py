from django.shortcuts import render
# from django.http.response import HttpResponse
from datetime import datetime

# Create your views here.
def greeting(request):
    return render(request, 'greetings/greetings.html')

def dtl(request):
    name = 'Engr. Matin'
    date_time = datetime.now()
    return render(request, 'greetings/dtl.html', context = {'nm':name, 'dt':date_time})
