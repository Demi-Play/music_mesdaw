
# Create your tests here.
# daw/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
import json
from .models import Project

# daw/tests.py
class DAWAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="pass")
        self.client.login(username="user", password="pass")

    def test_create_project(self):
        response = self.client.post('/api/daw/project/create/', {"name": "New Project"})
        self.assertEqual(response.status_code, 201)
        project = Project.objects.first()
        self.assertEqual(project.name, "New Project")

    def test_save_project(self):
        # Создаем проект с JSONField
        project = Project.objects.create(
            user=self.user, 
            name="Test Project", 
            tracks=[{'track_name': 'Track 1', 'volume': 0.8}], 
            mixer_settings={}
        )

        # Отправляем tracks и mixer_settings как JSON-данные без сериализации вручную
        response = self.client.post(f'/api/daw/project/{project.id}/save/', {
            'tracks': [{'track_name': 'Track 1', 'volume': 0.8}],  # Оставляем как список словарей
            'mixer_settings': {'eq': 'high'}
        }, content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        project.refresh_from_db()
        tracks = project.tracks  # JSONField автоматически десериализует JSON
        self.assertEqual(tracks[0]['track_name'], 'Track 1')


