from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from orders.models import Order
from orders.serializers import OrderSerializer


class OrdersListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CreateOrderAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DeleteOrderAPIView(APIView):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        serializer = OrderSerializer(instance=order)
        return Response(serializer.data)

    def delete(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        order.delete()
        return Response({'detail': 'success'}, status=status.HTTP_204_NO_CONTENT)
