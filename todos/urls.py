from todos.views import  CreateTodoAPIView, TodoDetailAPIView,TodoListAPIView,TodoCreateListAPIView
from django.urls import path


urlpatterns = [
    path('create', CreateTodoAPIView.as_view(), name="create-todo"),
    path('list', TodoListAPIView.as_view(), name='list_todo'),
    path('createlist', TodoCreateListAPIView.as_view(), name='create-list-todo'),
    path("<int:id>", TodoDetailAPIView.as_view(), name="detail")
]
