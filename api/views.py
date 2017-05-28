from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework import permissions
from .permissions import IsOwner
# Create your views here.

class GetView(generics.RetrieveUpdateDestroyAPIView):

    """This class handles the http GET requests."""


    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
