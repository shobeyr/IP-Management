from django.urls import path
from .views import GroupListCreate, ServerListCreate

urlpatterns = [
    path('api/groups/', GroupListCreate.as_view(), name='group-list'),
    path('api/servers/', ServerListCreate.as_view(), name='server-list'),
]
