from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from .serializers import *
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.

def index(request): 
    return render(request, 'index.html', {})


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class menuView(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = menu.objects.all()
    serializer_class = MenuSerializer
    
class singleMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

#@api_view()
#@permission_classes([IsAuthenticated])
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = booking.objects.all()
    serializer_class = BookingSerializer
    
    
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})