from django.urls import path
from django.http import HttpResponse
from .views import GroupListCreate, ServerListCreate

def home(request):
    return HttpResponse("<h1>Welcome to Abalon IP Management</h1>")

urlpatterns = [
    path('', home, name='home'),
    path('api/groups/', GroupListCreate.as_view(), name='group-list'),
    path('api/servers/', ServerListCreate.as_view(), name='server-list'),
]
