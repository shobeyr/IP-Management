from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

groups = []
servers = []

class GroupListCreate(APIView):
    def get(self, request):
        return Response(groups)

    def post(self, request):
        group = request.data
        groups.append(group)
        return Response(group, status=status.HTTP_201_CREATED)

class ServerListCreate(APIView):
    def get(self, request):
        return Response(servers)

    def post(self, request):
        server = request.data
        servers.append(server)
        return Response(server, status=status.HTTP_201_CREATED)
