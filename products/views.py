from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import OAuth2Authentication


class ProductView(APIView):

    def get(self, request):
        try:
            products = Product.objects.all()
            print(products)
            serializer = ProductSerializer(products , many=True)
                        
            return Response({'status':200, "data":serializer.data})
           
        except Exception as e:
            print(e)
            return Response({'error':e})


    def post(self,request):
        try:
            id = request.data.get('id')
            product = Product.objects.get(id=id)
            print(product)
            serializer= ProductSerializer(product)

     
            return Response({'status':200, 'data':serializer.data})

        except Exception as e:
            print(e)
            return Response({'error':e})




class CategoryView(APIView):
    
    def get(self, request):
        try:
            categories = Category.objects.all()
            serl = CategorySerializer(categories, many=True)
            return Response({'status':200, 'data':serl.data})


        except Exception as e:
            print(e)
            return Response({'error':e})




class CartView(APIView):
    
    # authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            cart = Cart.objects.filter(user = request.user)
            serl = CartSerializer(cart, many=True)
            # serl = CartSerializer(user=request.user)
            print(serl.data)

            return Response({'status':200, 'data':serl.data})


        except Exception as e:
            print(e)
            return Response({'error':e})

    def post(self, request):
        try:
            # CartSerializer(user=request.user)
            # print(serl.data)
            cart = Cart.objects.get(user=request.user)
            serializer = CartItemSerializer(data=request.data)
            if serializer.is_valid():
                cart_item = serializer.save()
                cart.items.add(cart_item)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({'error':e})