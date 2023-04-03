from rest_framework.serializers import ModelSerializer
from .models import Mmodal

class EmpSerializer(ModelSerializer):
    class Meta:
        model=Mmodal
        fields='__all__'