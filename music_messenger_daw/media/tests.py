from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import MediaFile

class MediaFileTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_file_upload(self):
        url = reverse("upload_media")
        with open("media/test_files/test_file.mp3", "rb") as test_file:
            response = self.client.post(url, {"file": test_file}, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("file_id", response.data)

    def test_file_download(self):
        # Загружаем тестовый файл и сохраняем его в базе данных
        with open("media/test_files/test_file.mp3", "rb") as test_file:
            media_file = MediaFile.objects.create(file="media/test_files/test_file.mp3")

        url = reverse("download_media", args=[media_file.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Disposition"], f"attachment; filename={media_file.file.name}")

    def test_invalid_file_upload(self):
        url = reverse("upload_media")
        response = self.client.post(url, {}, format="multipart")  # Не передаем файл
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["message"], "No file provided")  # Проверка сообщения

    def test_nonexistent_file_download(self):
        url = reverse("download_media", args=[999])  # Несуществующий ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
