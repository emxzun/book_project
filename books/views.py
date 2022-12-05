from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from books.models import Books
from books.serializers import BookSerializer


class ListCreateBookApiView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RetUpdDelBookApiView(generics.RetrieveUpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@api_view(['DELETE'])
def book_del_api_view(request, pk):
    try:
        book = Books.objects.get(id=pk)
        book_owner = book.owner
        user = request.user
        if book_owner == user:
            book.delete()
            return Response({'msg': 'Успешно удалено'}, status=status.HTTP_200_OK)
        return Response({'msg': 'Удалить книгу может только ее автор'}, status=status.HTTP_400_BAD_REQUEST)
    except Books.DoesNotExist:
        return Response({'msg': 'Нет такой книги'}, status=status.HTTP_400_BAD_REQUEST)
