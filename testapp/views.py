from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer

class TodoListAPIView(APIView):
    """
    API View to handle CRUD operations for Todo items.
    """

    def get(self, request):
        """
        Retrieve all todo items.
        """
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new todo item.
        """
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailAPIView(APIView):
    """
    API View to handle CRUD operations for a single Todo item.
    """

    def get_object(self, pk):
        """
        Helper method to retrieve a Todo object by its primary key.
        """
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return None

    def get(self, request, pk):
        """
        Retrieve a specific todo item.
        """
        todo = self.get_object(pk)
        if todo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update a specific todo item.
        """
        todo = self.get_object(pk)
        if todo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific todo item.
        """
        todo = self.get_object(pk)
        if todo is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)