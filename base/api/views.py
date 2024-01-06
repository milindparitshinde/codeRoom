from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RoomSerializer
from ..models import Room

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /aip/rooms/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def getRoom(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)