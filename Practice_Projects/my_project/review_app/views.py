from django.shortcuts import render
from review_app.forms import Reviewer
from django.http import HttpResponseRedirect
from .models import reviewer
# from django.http import HttpResponse

# Create your views here.
def customer(request):
    return render(request, 'reviews/reviews.html')

# def details(request):
#     obj = Reviewer(auto_id=True, label_suffix=' : ')
#     obj.order_fields(field_order=['name', 'mobile', 'email'])
#     return render(request, 'reviews/review_form.html', {'form':obj} )

def send(request):
    return render(request, 'reviews/submit.html')

def details(request):
    if request.method == 'POST':
        # print(request.POST)
        print('Used method: POST')
        obj = Reviewer(request.POST)
        if obj.is_valid():
            # print('This form is valid')
            # print(obj.cleaned_data)
            # print('email : ', obj.cleaned_data['email'])
            # print('password : ', obj.cleaned_data['password'])
            nam = obj.cleaned_data['name']
            mob = obj.cleaned_data['mobile']
            mail = obj.cleaned_data['email']
            pas = obj.cleaned_data['password']
            con_pas = obj.cleaned_data['confirm_password']
            rev = obj.cleaned_data['review']
            ag = obj.cleaned_data['age']
            gp = obj.cleaned_data['cgpa']
            tube = obj.cleaned_data['youtube']
            
            data = reviewer(name = nam, mobile = mob, email = mail, password = pas, confirm_password = con_pas, review = rev, age = ag, cgpa = gp, youtube = tube)
            data.save()
            return HttpResponseRedirect('/rev/ok')
    else:
        obj = Reviewer(auto_id=True, label_suffix=' : ')
        print('Used method: GET')
        
    return render(request, 'reviews/review_form.html', {'form':obj} )
