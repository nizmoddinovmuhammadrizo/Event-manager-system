from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.registration.models import Registration
from api.user.serializers import register_serializers


class RegistrationApiView(ListAPIView):
    serializer_class = register_serializers.RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)
