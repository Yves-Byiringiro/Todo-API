from django.utils import timezone
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import Todo




class CreateListTodo(APIView):
    def post(self,request):
        if request.method == "POST":
            form = CreateUpdateTodo(data=request.data)
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
                        status=status.HTTP_201_CREATED
                        )
                except:
                    return Response({"error":"something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            else:
                return Response({"error": form.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            todos = Todo.objects.all()
            serialized_todos = DisplayTodoSerialzer(todos, many=True)
            return Response({"todos": serialized_todos.data}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetUpdateDeleteTodo(APIView):

    def get(self, request, todo_id):
        try:
            todo = Todo.objects.get(id=todo_id)
            return Response({"book":DisplayTodoSerialzer(todo).data}, status=status.HTTP_200_OK)
        
        except:
            return Response({"error":"something went wrong"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, todo_id):
        try:
            todo = Todo.objects.get(id=todo_id)
        except Exception as e:
            return Response({"error":"something went wrong"}, status=status.HTTP_404_NOT_FOUND)

        form = CreateUpdateTodo(data=request.data)
        try:
            if form.is_valid():
                todo.title =  form.data.get('title')
                todo.description =  form.data.get('description')
                todo.priority = form.data.get('priority')
                todo.modifiedDate = timezone.now()
                todo.save()
                return Response(
                    {"todo":DisplayTodoSerialzer(todo).data,
                    "message":"Todo has been updated successfully"},
                    status=status.HTTP_200_OK
                    )
        except:
            return Response({"error":"something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, todo_id):
        try:
            todo = Todo.objects.get(id=todo_id)
        except Exception as e:
            print("***************************************")
            print(e)
            print("***************************************")

            return Response({"error":"something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        todo.delete()
        return Response({"message":"Todo deleted successfully"}, status=status.HTTP_200_OK)

