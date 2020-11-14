from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tutorial.quickstart.models import Books
from tutorial.quickstart.serializers import BooksSerializer

@api_view(['GET', 'POST'])
def books(request):
    # Listado de libros
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

    # Crea un libro
    elif request.method == 'POST':
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book(request, pk):
    # Consulta el libro
    try:
        book = Books.objects.get(pk=pk)
    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Devuelve el libro
    if request.method == 'GET':
        serializer = BooksSerializer(book)
        return Response(serializer.data)

    # Actualiza el libro
    elif request.method == 'PUT':
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Elimina el libro
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)