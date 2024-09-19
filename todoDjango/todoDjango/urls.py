from django.urls import path, include
from web import views


tasks_url = [
    path('', views.tasks),
    path('new', views.new_task),
    path('delete', views.delete_task),
]


urlpatterns = [
    path('', views.index),
    path('tasks/', include(tasks_url))
]
