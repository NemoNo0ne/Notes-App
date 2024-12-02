from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteTests(TestCase):

    def setUp(self):
        # Создание текстовой заметки
        self.note = Note.objects.create(
            title='Test Note',
            content='This is a test note.',
            priority=1
        )

    def test_note_list_view(self):
        # Проверяем доступность списка заметок
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertTemplateUsed(response, 'notes/note_list.html')

    def test_note_detail_view(self):
        # Проверяем отображение деталей зкаметки
        response = self.client.get(reverse('note_detail', args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test note.')
        self.assertTemplateUsed(response, 'notes/note_detail.html')

    def test_note_create_view(self):
        # Проверяем создание новой заметки
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'Content of new note',
            'priority': 2,
        })
        self.assertEqual(response.status_code, 302) # Перенаправление после создания
        self.assertEqual(Note.objects.last().title, 'New Note')

    def test_note_edit_view(self):
        # Проверяем редактирование заметки
        response = self.client.post(reverse('note_edit', args=[self.note.pk]), {
            'title': "Updated Note",
            'content': "Updated content",
            'priority': 2,
        })
        self.assertEqual(response.status_code, 302) # Перенаправление после редактирования
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_note_delete_view(self):
        # Проверяем удаление заметки
        response = self.client.post(reverse('note_delete', args=[self.note.pk]))
        self.assertEqual(response.status_code, 302) # Перенаправление после удаления
        self.assertFalse(Note.objects.filter(pk=self.note.pk).exists())
