
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from leads.api.serializers import LeadSerializer, UserSerializer
from leads.models import Lead
from django.contrib.auth.models import User



@api_view(['GET',])
def leadList(request):
    # return Response({"message": "Hello, World!"})
    
    serializer = LeadSerializer(Lead.objects.all(), many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET',])
def userList(request):
    # return Response({"message": "Hello, World!"})
    
    serializer = UserSerializer(User.objects.all(), many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET',])
def userLeadList(request, id):
    # return Response({"message": "Hello, World!"})
    
    serializer = LeadSerializer(Lead.objects.filter(user_id=id), many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST',])
def createLead(request, pk):
    # return Response({"message": "Hello, World!"})
    user = User.objects.get(pk=pk)
    lead = Lead(user=user)

    if request.method == "POST":
        serializer = LeadSerializer(lead, data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT',])
def updateLeadList(request, id):
    # return Response({"message": "Hello, World!"})
    
    serializer = LeadSerializer(Lead.objects.get(id=id), data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "Update Successfull"
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# class ListLeads(APIView):
#     http_method_names = ['get', 'head']
#     def get(self, request, format=None):
#         # import pdb; pdb.set_trace()
#         serializer = LeadSerializer(Lead.objects.all(), many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)