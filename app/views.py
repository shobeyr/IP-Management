from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# لیست‌ها برای ذخیره گروه‌ها و سرورها (به صورت موقت)
groups = []
servers = []

# 🌟 صفحه اصلی (Homepage)
def home(request):
    return render(request, 'index.html')

# 🌐 مدیریت گروه‌ها (APIView برای گروه‌ها)
class GroupListCreate(APIView):
    def get(self, request):
        # لیست گروه‌ها را برمی‌گرداند
        return Response(groups)

    def post(self, request):
        group = request.data
        groups.append(group)
        return Response(group, status=status.HTTP_201_CREATED)

    def delete(self, request):
        group_name = request.data.get("name")
        global groups
        groups = [g for g in groups if g.get("name") != group_name]
        return Response({"message": "Group deleted"}, status=status.HTTP_200_OK)

# 🌐 مدیریت سرورها (APIView برای سرورها)
class ServerListCreate(APIView):
    def get(self, request):
        # لیست سرورها را برمی‌گرداند
        return Response(servers)

    def post(self, request):
        server = request.data
        servers.append(server)
        return Response(server, status=status.HTTP_201_CREATED)

    def delete(self, request):
        server_name = request.data.get("name")
        global servers
        servers = [s for s in servers if s.get("name") != server_name]
        return Response({"message": "Server deleted"}, status=status.HTTP_200_OK)
