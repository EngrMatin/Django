from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,])    # This permission_classes will override the DEFAULT_PERMISSION_CLASSES in settings.py
def secondAPI(request):
    if request.method == 'POST':
        name = request.data['name']
        age = request.data['age']
        return Response({"name": name, "age": age})
    
    context = {
        "name": "Rakib app2",
        "university": "RUET"
    }
    return Response(context)

# creating a registration API using a simple method similar to django
from django.contrib.auth.models import User

@api_view(['POST'])
def registrationAPI(request):
    if request.method == 'POST':
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1 = request.data['password1']
        password2 = request.data['password2']
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'An user with that username already exists!'})
        if password1 != password2:
            return Response({'error': "Two passwords didn't matched!"})
        
        user = User()
        
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True
        
        user.set_password(raw_password=password1)
        user.save()
        
        return Response({'Success': 'User successfully registered!'})


# # Simple API View without serializer
# # Function based
# from .models import *

# # @api_view(['POST',])
# # def contactpost(request):
# #     if request.method == 'POST':

# # Class based
# from rest_framework.views import APIView

# class ContactAPIView(APIView):
#     permission_classes = [AllowAny,]
    
#     def post(self, request, format=None):
#         name = request.data['name']
#         email = request.data['email']
#         subject = request.data['subject']
#         phone = request.data['phone']
#         details = request.data['details']
        
#         contact = Contact(name=name, email=email, subject=subject, phone=phone, details=details)
#         contact.save()
        
#         return Response({'success': 'Successfully saved!'})
    
#     def get(self, request, format=None):
#         return Response({'success': 'Successfully saved from GET!'})


from rest_framework.views import APIView
from . models import *
from .serializers import *

class ContactAPIView(APIView):
    permission_classes = [AllowAny,]
    
    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
        # return Response({'success': 'Successfully saved!'})
    
    def get(self, request, format=None):
        queryset = Contact.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)
        # return Response({'success': 'Successfully saved from GET!'})

