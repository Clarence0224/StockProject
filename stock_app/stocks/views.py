from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Stock
from .serializers import stockSerializer
from rest_framework.decorators import api_view
from django.shortcuts import render

def openDashboard(request):
    return render(request, 'stocks/Dashboard.html')

@api_view(['GET'])
def ShowAll(request):
    allstocks = Stock.objects.all()
    serializer = stockSerializer(allstocks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewStock(request, pk):
    mystock = Stock.objects.get(id=pk)
    serializer = stockSerializer(mystock, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def BuyStock(request):
    serializer = stockSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def SellStock(request, pk):
    mystock = Stock.objects.get(id=pk)
    mystock.delete()
    return Response('Stock sold successfully!')

