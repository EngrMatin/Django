# django function based view
# from django.shortcuts import render

# def homeview(request):   
#     if request.method=='POST':
#         name = request.POST['name']  
#         email = request.POST['email']    
#         photo = request.FILES['photo']    
#     context={
#         'name': 'Sadman',
#         'university': 'DUET'
#     }
#     return render(request, 'home.html', context)

# django class based view
from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):   
    
        context={
            'name': 'Sadman Sakib',
            'university': 'DUET'
        }
        return render(request, 'home.html', context)


# REST API function based view
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['GET','POST'])     
# def homeAPI(request):   
#     if request.method=='POST':
#         name = request.data['name']  
#         email = request.data['email']       
#         photo = request.FILES['photo']       
#     context={
#         'name': 'Sadman',
#         'university': 'DUET'
#     }
#     return Response(context)

# REST API class based view
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeAPIView(APIView):     
    def get(self, request, format=None):   
        context={
            'name': 'Sadman Sakib',
            'university': 'DUET'
        }
        return Response(context)

