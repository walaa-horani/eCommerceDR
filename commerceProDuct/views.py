from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ProductSerializer,CartItemSerializer
from .models import Product, CartItem


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    @action(detail=True, methods=['get'])
    def total_price(self, request, pk=None):
        cart_item = self.get_object()
        total_price = cart_item.product.price * cart_item.quantity
        return Response({'total_price': total_price})



    @action(detail=False, methods=['get'])
    def view_cart(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        serializer = self.get_serializer(cart_items, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        product = Product.objects.get(id=pk)
        cart_item, created = CartItem.objects.get_or_create(
            product=product, user=request.user
        )
        cart_item.quantity += 1
        cart_item.save()
        serializer = self.get_serializer(cart_item)
        return Response(serializer.data)

    @action(detail=True, methods=['delete'])
    def remove_from_cart(self, request, pk=None):
        cart_item = self.get_object()
        cart_item.delete()
        return Response({'detail': 'Item removed from cart'})


