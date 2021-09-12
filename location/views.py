from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LocationSerializer

class LocationView(APIView):
    # def get(self, request):
    #     pass

    def post(self, request):
        try:
            response = {}
            serializer = LocationSerializer(data=request.data)
            if(serializer.is_valid(raise_exception=True)):
                serializer.save()
                response['msg'] = 'Location added!'
                return Response(response, status=status.HTTP_200_OK)
            response['msg'] = serializer.error_messages
        except Exception as e:
            response['error'] = str(e)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
