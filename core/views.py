from django.utils import timezone
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import Todo




class CreateListTodos(APIView):
    def post(self,request):
        if request.method == "POST":
            form = RegisterTodo(data=request.data)
            if form.is_valid():
                try:
                    title = form.data.get('title')
                    description = form.data.get('description')
                    priority = form.data.get('priority')
                    todo = Todo.objects.create(title=title,description=description,priority=priority)
                    todo.save()
                    return Response(
                        {"message":"todo created successfully",
                        "id":todo.id,
                        "title":todo.title,
                        "description":todo.description,
                        "created_date":todo.createDate},
                        status=status.HTTP_200_OK
                        )
                except Exception as e:
                    print("*"*20)
                    print(e)
                    print("*"*20)

                    return Response({"error":"something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            else:
                return Response({"error": form.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            todos = Todo.objects.all()
            serialized_todos = DisplayTodoSerialzer(todos, many=True)
            return Response({"todos": serialized_todos.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print("*"*20)
            print(e)
            print("*"*20)
            return Response({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

