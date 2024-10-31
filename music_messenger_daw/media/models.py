from django.db import models
# from cryptography.fernet import Fernet

# Генерируем ключ, или указываем его из переменных окружения
# key = b'afSgHF-TdlML7_kXgv3zDpxyvkFWFvKgs_mPStYFscg='  # Замените ключ на переменную окружения для безопасности
# cipher_suite = Fernet(key)

class MediaFile(models.Model):
    file = models.FileField(upload_to='media/')
    metadata = models.JSONField(null=True, blank=True)
    # file = models.FileField(upload_to='media/')
    # encrypted_content = models.BinaryField()
    # metadata = models.JSONField()

    # def save(self, *args, **kwargs):
    #     # Открываем файл и читаем содержимое для шифрования
    #     with self.file.open('rb') as f:
    #         file_data = f.read()
    #         self.encrypted_content = cipher_suite.encrypt(file_data)
    #     super().save(*args, **kwargs)
