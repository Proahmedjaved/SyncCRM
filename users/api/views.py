
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from users.api.serializers import RegistrationSerializer
from leads.api.serializers import UserSerializer
from leads.models import Lead
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@api_view(['POST',])
def registraion_view(request):
    # return Response({"message": "Hello, World!"})
    
    serializer = RegistrationSerializer(data=request.data)
    data= {}
    if serializer.is_valid():
        user = serializer.save()
        data['token'] = Token.objects.get(user=user).key
        data['response'] = "User registration successfull"
        data["email"] = user.email
        data['username'] = user.username
    else:
        data = serializer.errors
    return Response(data)

# @api_view(['POST',])
# def obt_auth_view(request):
#     data1 = {}
#     if request.data:
#         data = request.data
#         user = User.objects.get(username=data['username'])
#         print(data['password'])
#         print(user.password)
#         if data['password'] == user.password:
#             data1['token'] = Token.objects.get(user=user).key
        
#     return Response(data1)