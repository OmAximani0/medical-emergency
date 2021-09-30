from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LocationSerializer
from .models import Location
from twilio.rest import Client
import os

class AddLocationView(APIView):

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    try:
        def post(self, request):
            try:
                response = {}
                serializer = LocationSerializer(data=request.data)
                if(serializer.is_valid(raise_exception=True)):
                    serializer.save()
                    self.send_sms(serializer.validated_data)
                    serializer.sendToClient()
                    response['msg'] = 'Location added!'
                    return Response(response, status=status.HTTP_200_OK)
                response['msg'] = serializer.error_messages
            except Exception as e:
                response['error'] = str(e)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)

    def send_sms(self, data):
        self.client.messages.create(
            body=f"Lat: {data.get('lat')} \nLang: {data.get('long')} \nVehicle No.: {data.get('vehicle_no')} \nDevice ID: {data.get('device_id')}",
            from_='+12058393425',
            to=str(os.environ['TO'])
        )

class AllLocationView(APIView):
    try:
        def get(self, request):
            instance = Location.objects.all()
            serializer = LocationSerializer(instance, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)