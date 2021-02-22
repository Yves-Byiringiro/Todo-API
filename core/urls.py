from django.urls import path
from .views import *


urlpatterns = [

    path('todos/', CreateListTodos.as_view()),
]
