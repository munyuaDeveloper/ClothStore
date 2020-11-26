from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from APIs.product_api.serializers import ProductSerializer, CategorySerializer
from products.models import Product, Category


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(APIView):
    serializer_class = ProductSerializer

    def get(self, request):
        product_id = request.query_params.get('id')
        product_instance = Product.objects.filter(id=product_id).first()
        if not product_instance:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(instance=product_instance)
        return Response(serializer.data)
