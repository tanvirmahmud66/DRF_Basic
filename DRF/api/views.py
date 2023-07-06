from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Books
from .serializers import BooksSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
def api_overview(request):
    all_api = {
        "book-list": '/book-list/',
        "create-new-list_item": '/book-create/',
        "single_book-update-delete": '/book-id/',
    }
    return JsonResponse(all_api)

#-------------------------------------------------------------- /book-list/
# def book_list(request):
#     books = Books.objects.all() #complex data-structure
#     book_list = list(books.values()) #python data-structure
#     return JsonResponse({
#         "books": book_list,
#     })

@api_view(['GET'])
def book_list(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books, many=True)
    return Response(serializer.data)


#---------------------------------------------------------------- /book-create/
@api_view(['POST'])
def book_create(request):
    serializer = BooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#----------------------------------------------------------------- /book-id/
@api_view(['GET', 'PUT', 'DELETE'])
def book_single(request, pk):
    #ger the target book
    try:
        book = Books.objects.get(id=pk)
    except Exception as E:
        print(E)
        return Response({
            "error": f"book-id:{pk} doesn't exit in database"
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Get method
    if request.method == 'GET':
        serializer = BooksSerializer(book, many=False)
        return Response(serializer.data)
    
    #Update
    if request.method == "PUT":
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Delete
    if request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

