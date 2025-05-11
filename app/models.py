# models.py
from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Server(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='servers')
    server_name = models.CharField(max_length=100)
    dc_name = models.CharField(max_length=100)
    public_ip = models.GenericIPAddressField()
    private_ip = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.server_name} - {self.public_ip}"
