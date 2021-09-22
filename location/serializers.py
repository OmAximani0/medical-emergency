from rest_framework.serializers import ModelSerializer
from .models import Location
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class LocationSerializer(ModelSerializer):
    def sendToClient(self):
        channel_layer = get_channel_layer()
        instance = Location.objects.filter(hasSent=False)
        async_to_sync(channel_layer.group_send)(
            '_location_group', {
                'type': 'send_loc',
                'value': json.dumps(LocationSerializer(instance, many=True).data)
            }
        )
        Location.objects.filter(hasSent=False).update(hasSent=True)

    class Meta:
        model = Location
        fields = '__all__'