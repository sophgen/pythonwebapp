from apis.serializers import order_api_serializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from order_entry.models import order
from rest_framework import status , generics


class order_data(generics.GenericAPIView):
    queryset = order.objects.all()
    serializer_class = order_api_serializer
    permission_classes = [IsAuthenticated,]

    def get(self, request, format=None):
        orders = order.objects.all()
        serializer = order_api_serializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = order_api_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)