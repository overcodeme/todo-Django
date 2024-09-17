from django.urls import path, include
from web import views


tasks = [
    path('', views.tasks),
    path('new', views.new_task),
    path('delete', views.delete_task),
    path('details', views.task_info)
]


urlpatterns = [
    path('', views.index),
    path('tasks/', include(tasks))
]
