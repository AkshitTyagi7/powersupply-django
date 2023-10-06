from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def getData(request):
    try:
        productCode=request.data.get('productCode')  
        fromDate=request.data.get('fromDate')
        noToken=request.data.get('numberOfTokens')
        toDate=request.data.get('toDate')
        url="https://www.iexindia.com/IEXPublish/AppServices.svc/IEXGetTradeData"
        """ body={
            "APITokenNo":"NCLIEXHkl7900@8Uyhkj", "Product_Code":1, "From_Date":"20/02/2022", "From_Token":1, "To_Date":"21/02/2022",
    "To_Token":10,
    "Date_Type":2
        } """
        print(productCode,fromDate,noToken,toDate)
        body={
            "APITokenNo":"NCLIEXHkl7900@8Uyhkj",
            "Product_Code":productCode,
            "From_Date":fromDate,
            "From_Token":1,
            "To_Date":toDate,
            "To_Token":noToken,
            "Date_Type":2
        }
        data= requests.post(url, json = body, headers={'Content-Type': 'application/json'})
        """ Return just data as a api response """
        print('-----------------')
        print(data.request.body)
        return Response({
            'data': data.json(),
        })
    except Exception as e:
        print(e)
        return Response({
            'data': [],
        })
