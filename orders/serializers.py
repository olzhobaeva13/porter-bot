from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'name', 'phone_number', 'porter',
                  'movers', 'dispersal', 'trash', 'description', ]

    def create(self, validated_data):
        instance = Order.objects.create(
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            porter=validated_data['porter'],
            movers=validated_data['movers'],
            dispersal=validated_data['dispersal'],
            trash=validated_data['trash'],
            description=validated_data['description'],
        )
        return instance
       