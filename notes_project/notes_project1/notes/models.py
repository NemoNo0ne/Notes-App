from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")  # Заголовок заметки
    content = models.TextField(verbose_name="Content")  # Текст заметки
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")  # Время создания
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")  # Время последнего обновления
    priority = models.IntegerField(default=0, verbose_name="Priority")  # Приоритет заметки

    def __str__(self):
        return self.title
