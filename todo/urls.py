from django.urls import path,include
from . import views
from .views import TodoDelete,TodoUpdate

urlpatterns = [
    path('', views.index_view,name='index'),
    path('complete', views.complete_view,name='complete'),
    path('create', views.create_todo,name='create'),
    path('delete/<int:pk>',TodoDelete.as_view(),name='delete'),
    path('update/<int:pk>',TodoUpdate.as_view(),name='update'),
    path('complete_task/<int:pk>', views.complete_task, name='complete_task'),

]