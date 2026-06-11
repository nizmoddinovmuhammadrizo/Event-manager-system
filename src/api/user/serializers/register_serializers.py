from rest_framework.serializers import ModelSerializer
from apps.registration.models import Registration


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'