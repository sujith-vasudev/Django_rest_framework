from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import employees
from .serializers import employeesSerializers

# Create your views here.

@api_view(['GET','POST'])
def CRUD(request):
    if request.method == 'GET':
        employees1 = employees.objects.all()
        serializer = employeesSerializers(employees1,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = employeesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        pass


