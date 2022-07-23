from django.urls import path

from orders.views import OrdersListAPIView, CreateOrderAPIView, DeleteOrderAPIView


urlpatterns = [
    path('', OrdersListAPIView.as_view()),
    path('create/', CreateOrderAPIView.as_view()),
    path('<int:order_id>/delete/', DeleteOrderAPIView.as_view())
]
