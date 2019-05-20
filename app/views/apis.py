from rest_framework import viewsets
from django.shortcuts import render

from app.serializers import CategorySerializer
from app.serializers import OrderSerializer
from app.serializers import TodoSerializer
from app.serializers import UserSerializer

from app.models.category import Category
from app.models.order import Order
from app.models.todo import Todo
from app.models.user import User

from datetime import datetime

# DRF
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save()

    # def perform_update(self, serializer):
    #     serializer.save()
    #
    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
