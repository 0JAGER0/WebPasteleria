from django.shortcuts import render
from rest_framework import serializers
from rest_framework import permissions
from core.models import listadoTortas
from .serializers import TortaSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def apiTortas(request):
    if request.method == 'GET':
        """
        LISTA DE TODAS LAS TORTAS
        """
        tortaa = listadoTortas.objects.all()
        serializer = TortaSerializer(tortaa, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser.parse(request)
        serializer = TortaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def torta(request,pk):
    try:
        tortaa = listadoTortas.objects.get(idtorta=pk)
    except listadoTortas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """ 
    GET: mostrar detalle de un torta segun id
    """        
    if request.method == 'GET':
        serializer = TortaSerializer(tortaa)
        return Response(serializer.data)

        
    elif request.method == 'PUT':
        """
        PUT: editar un torta por id
        """
        data = JSONParser().parse(request)
        serializer = TortaSerializer(tortaa,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        """
        DELETE: Borrar un torta por id
        """
        tortaa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)







