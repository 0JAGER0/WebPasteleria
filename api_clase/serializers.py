from rest_framework import fields, serializers
from core.models import listadoTortas

class TortaSerializer(serializers.ModelSerializer):
    class Meta:
        model = listadoTortas
        fields = ['idtorta','torta','tipotorta','tamanio','stock']


