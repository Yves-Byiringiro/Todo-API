from django.urls import path
from .views import *


urlpatterns = [

    path('todos/', CreateListTodo.as_view()),
    path('todo/details/<int:todo_id>/', GetUpdateDeleteTodo.as_view()),
    path('todo/search/<str:todo_q>/', SearchTodo.as_view())

]
