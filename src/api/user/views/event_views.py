from rest_framework.generics import ListAPIView
from apps.events.models import Event
from api.user.serializers import event_serializers


class EventApiView(ListAPIView):
    serializer_class = event_serializers.EventListSerializer

    def get_queryset(self):
        return Event.objects.filter(is_active=True)
