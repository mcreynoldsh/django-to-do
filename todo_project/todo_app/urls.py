from django.urls import path 
from . import views


urlpatterns = [

    path('signup', views.sign_up),
    path('login', views.log_in),
    path('logout', views.log_out),
    path('todos/new', views.new_todo),
    path('todos', views.view_todos),
    path('todos/<int:id>', views.todo_detail),
    path('todos/<int:id>/edit', views.edit_todo),
    path('todos/<int:id>/delete', views.delete_todo)
]