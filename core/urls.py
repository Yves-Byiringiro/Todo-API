from django.urls import path
from .views import *


urlpatterns = [

    path('todos/', CreateListTodos.as_view()),
    path('todo/details/<int:todo_id>/', GetUpdateDeleteSearch.as_view())
]
