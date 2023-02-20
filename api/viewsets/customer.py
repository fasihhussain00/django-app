from rest_framework.response import Response
from rest_framework.request import Request 
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from ..models import Customer, CustomerSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(methods=['get'], detail=False)
    def filter(self, request: Request):
        filter = {
            'name': request.query_params.get('name') 
        }
        for filter_name, filter_value in filter.items():
            if filter_value is not None:
                self.queryset = self.queryset.filter(**{filter_name: filter_value})
        serializer = self.get_serializer_class()(self.queryset, many=True)
        return Response(serializer.data)