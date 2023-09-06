from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Calculation
from .serializers import CalculationSerializer

@api_view(['POST'])
def evaluate_expression(request):
    if request.method == 'POST':
        serializer = CalculationSerializer(data=request.data)
        if serializer.is_valid():
            expression = serializer.validated_data['expression']
            try:
                result = eval(expression)
                calculation = Calculation.objects.create(expression=expression, result=result)
                return Response({'result': result}, status=200)
            except Exception as e:
                return Response({'error': str(e)}, status=400)
        return Response(serializer.errors, status=400)
