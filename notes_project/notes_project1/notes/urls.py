from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name = 'note_list'), # Просмотр всех заметок
    path('note/<int:pk>/', views.note_detail, name = 'note_detail'), # Детали заметок
    path('note/new/', views.note_create, name = 'note_create'), # Создание заметок
    path('note/<int:pk>/edit/', views.note_edit, name = 'note_edit'),# Редактирование заметок
    path('note/<int:pk>/delete/', views.note_delete, name = 'note_delete'), # Удаление заметок
]