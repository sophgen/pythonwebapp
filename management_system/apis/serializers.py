from rest_framework import serializers
from order_entry.models import order


class order_api_serializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'